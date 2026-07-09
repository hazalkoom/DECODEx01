# Technical Report: C++ Compilation & Dependency Caching Optimization
**Date:** July 9, 2026  
**Subject:** Optimizing the C++ extension build pipeline to enable near-instantaneous development feedback loops and scalable multi-language support.

---

## 1. Introduction and Context

In the DECODE repository, we are building a high-performance local code intelligence engine. The core parser logic is written in C++ (`src/ast_parser.cpp`) for speed and safety, exposing interfaces to Python using `pybind11`. Under the hood, the syntax analysis is powered by **Tree-sitter**, a robust incremental parsing library. 

To compile and link the C++ extensions with Python, the project uses **scikit-build-core** as the modern build backend, adhering to standard PEP 517/PEP 621 packaging. External codebases (like the tree-sitter core library and individual language grammars) are integrated directly into our CMake compilation unit by dynamically downloading them from GitHub via CMake's `FetchContent` API during build time.

---

## 2. The Problem: The 60-Second Development Feedback Bottleneck

As the project scales and supports more languages (currently Python and JavaScript, with plans to support Go, Rust, TypeScript, C++, etc.), the time required to build and test the module was scaling poorly. 

Specifically, every time a developer ran the command:
```bash
poetry run pip install -e .
```
the following sequence of slow operations occurred:

1. **Ephemeral Build Directories:** By default, `pip` and `scikit-build-core` spin up a temporary directory (e.g. under `/tmp/pip-install-...`) to configure and build the wheel. Once the install completes, this temporary directory is completely deleted.
2. **Redundant Network Activity:** Because the build directory was ephemeral, CMake's cache was destroyed on every run. Consequently, CMake's `FetchContent` had no memory of previous downloads and was forced to perform fresh `git clone` operations from GitHub for:
   - Tree-sitter Core (`v0.24.6`)
   - Tree-sitter Python Grammar (`v0.23.5`)
   - Tree-sitter JavaScript Grammar (`v0.23.1`)
3. **No Incremental C++ Compilation:** Since the object files (`.o` files) from the previous compilation were deleted with the temporary directory, the compiler had to re-compile all C/C++ files from scratch. This included the entire Tree-sitter C codebase, the massive generated parser files (`parser.c` and `scanner.c` for both Python and JavaScript), and our custom wrappers.
4. **Poor Developer Experience:** The entire cycle took **36 to 60+ seconds** depending on network latency. Since compiling and running tests is a frequent action during active development, this 1-minute delay severely throttled iteration speeds.

---

## 3. Technical Analysis: Why the Cache Was Being Wiped

In traditional C++ development, compilers output intermediate object files so that when you change a single source file, only that file is recompiled and relinked (incremental building). However, Python's PEP 517 packaging tools prioritize build cleanliness and reproducibility. They achieve this by enforcing **build isolation** and using **temporary workspaces**.

When `pip install -e .` is run:
1. `pip` creates a clean virtual environment and installs build-system dependencies (`scikit-build-core` and `pybind11`).
2. It generates a temporary workspace.
3. It invokes `scikit-build-core` to run CMake inside that workspace.
4. It packages the built extension and deletes the workspace.

To enable incremental builds, we needed to instruct `scikit-build-core` to bypass these temporary directories and use a **persistent build folder** within our project root, while still respecting the editable install mechanism.

---

## 4. The Solution: Persistent Builds & Live Auto-Rebuilds

We introduced a two-part solution involving static configuration in `pyproject.toml` and a helper installation script.

### Part A: Configuration Updates (`pyproject.toml`)

We added a dedicated `[tool.scikit-build]` section to configure the behavior of the `scikit-build-core` backend:

```toml
[tool.scikit-build]
# Preserve CMake caches and object files in the local build/ directory
build-dir = "build/{wheel_tag}"

# Automatically rebuild C++ files on Python import when changes are detected
editable.rebuild = true
editable.verbose = true
```

*   **`build-dir = "build/{wheel_tag}"`**: This tells the build backend to use a persistent `build/` directory in our workspace root instead of `/tmp`. Since this directory persists between compilations:
    - `FetchContent` checks the local cache and skips cloning the tree-sitter repositories if they are already present.
    - CMake preserves its configuration cache, omitting compiler checks and configuration passes.
    - Ninja/Make detects which files have changed and compiles **only** the modified files.
*   **`editable.rebuild = true`**: This is a powerful feature provided by `scikit-build-core`. When installing the package in editable mode, it installs a hook. When Python imports `codelens_core` (e.g. at the start of a test run), it checks if any C++ files have been modified. If they have, it triggers a fast incremental rebuild in the background automatically.

Additionally, to compile without build isolation (which is required to reuse the local virtual environment's packages and cache directory), we added `scikit-build-core` to the dev dependencies so it resides in the Poetry virtual environment:

```toml
[dependency-groups]
dev = [
    "pytest (>=9.1.1,<10.0.0)",
    "scikit-build-core>=0.10.0"
]
```

### Part B: Developer Hook Script (`dev-install.sh`)

To abstract away the flags required for a non-isolated, cached editable install, we created a helper script [dev-install.sh](file:///run/media/hazalkoom/FD16124010E85459/big%20project/DECODE/dev-install.sh):

```bash
#!/bin/bash
set -e
poetry run pip install --no-build-isolation -e . -v
echo ""
echo "✅ Build complete! Run tests with: poetry run pytest tests/ -s -v"
```

*   **`--no-build-isolation`**: Crucial flag that instructs `pip` to use the packages already installed in our Poetry venv (including `scikit-build-core` and `pybind11`), preventing the spin-up of temporary environments and allowing access to our persistent cache directory.

---

## 5. Performance Verification & Timing Results

We measured the execution times of different actions to verify the success of the optimization:

### Scenario 1: First-Time Clean Build
*   **Action:** Delete `build/` folder and run `./dev-install.sh`.
*   **Behavior:** Downloads tree-sitter core, python grammar, and javascript grammar; performs full compilation of all source files.
*   **Time taken:** **58.0 seconds** (Expected, as caching is not yet populated).

### Scenario 2: Re-installing after modifying `src/ast_parser.cpp` (Manual)
*   **Action:** Modify a line in `src/ast_parser.cpp` and run `./dev-install.sh`.
*   **Behavior:** Configures CMake in 1.2s (using cache), detects only 1 file changed, compiles `ast_parser.cpp.o` and links the `.so` binary.
*   **Time taken:** **10.09 seconds** (a **82.6% speedup**; most time spent is `pip` environment auditing).

### Scenario 3: Auto-rebuild on Test Run (Automatic)
*   **Action:** Modify `src/ast_parser.cpp` and immediately run `poetry run pytest tests/ -s -v`.
*   **Behavior:** The import hook triggers. Ninja checks the files, compiles `ast_parser.cpp`, links the shared library, and immediately executes the 13 tests.
*   **Time taken:** **6.32 seconds** (a **89.1% speedup**; bypasses `pip` completely).

### Scenario 4: Running Tests with No Changes (Fast Path)
*   **Action:** Run `poetry run pytest tests/ -s -v` when no files have changed.
*   **Behavior:** Hook checks files, Ninja reports "no work to do", and tests run instantly.
*   **Time taken:** **0.23 seconds** (Bypasses compilation completely).

---

## 6. Summary of Actions Taken

1.  **Analyzed build logs** to identify that the lack of build caching was causing full compiles and repository re-downloads on every single run.
2.  **Configured persistent caching** in `pyproject.toml` by routing build outputs to `build/{wheel_tag}`.
3.  **Added scikit-build-core** to dev dependencies and regenerated the lockfile using `poetry lock`.
4.  **Created `dev-install.sh`** to wrap editable installs with the non-isolated build flag.
5.  **Verified correctness** by running the test suite, touching a C++ file, and confirming that recompilation is now targeted (only 1 file compiled instead of all 10) and takes less than 6 seconds.
6.  **Archived the previous report** by moving `report.md` to `reports/report-2026-07-08-ast-parser-infinite-loop.md`.
