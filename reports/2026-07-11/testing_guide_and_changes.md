# DECODE Testing Guide and Change Report
**Date:** July 11, 2026

## 1. What We Changed
We successfully integrated three major Quality Assurance (QA) tools into the DECODE engine to ensure our C++ code is robust, memory-safe, and well-tested. Here are the files we modified to achieve this:

1. **`CMakeLists.txt`**
   - **What changed:** We added two new compilation flags: `ENABLE_SANITIZERS` and `ENABLE_COVERAGE`. We also wrapped the Python Pybind11 module in an `if(BUILD_PYTHON_MODULE)` block.
   - **Why:** This allows us to compile our C++ code with special tracking tools injected into it. We explicitly *exclude* the Python module from these tools because running memory sanitizers on Python shared libraries crashes the standard Python interpreter.

2. **`pyproject.toml`**
   - **What changed:** We added `pytest-cov`, `mutmut`, and `gcovr` to our development dependencies. We also added configuration sections at the bottom for `pytest` and `mutmut`.
   - **Why:** These are the Python tools that generate our HTML coverage reports and handle mutation testing configuration.

3. **`tests/cpp/test_ast_parser.cpp`**
   - **What changed:** We fixed an outdated assertion in our native C++ tests. A test was checking for `imported_name` to be `"loads"`, but we previously simplified our Tree-sitter query to only capture the `module_name`.
   - **Why:** When we ran the tests under the new ASan environment, this test failed (due to logic, not memory). We fixed the test expectation to match the actual, correct engine behavior.

4. **New Scripts (`run_asan.sh` and `run_coverage.sh`)**
   - **What changed:** We created two dedicated bash scripts in the root directory.
   - **Why:** They automatically handle the complex process of creating separate build directories (`build/asan/` and `build/coverage/`), compiling the C++ code with the correct CMake flags, running the tests, and generating the HTML reports.

---

## 2. How to Run All the Tests
We now have three different ways to run tests depending on what you want to check.

### A. The Standard Development Build (Fastest)
Use this during regular development when you are writing code and want quick feedback. This uses our persistent cache and takes less than 2 seconds.

```bash
# Compile the engine (fast incremental build)
./dev-install.sh

# Run the 46 Python integration and fuzzing tests
poetry run pytest tests/
```

### B. The Memory Safety Check (AddressSanitizer)
Use this when you have written complex C++ pointer logic or made changes to how we parse ASTs. It recompiles the C++ test suite with Google's AddressSanitizer injected into the binary to detect memory leaks, buffer overflows, and use-after-free bugs.

```bash
# Compile and run native C++ tests with memory checking
./run_asan.sh
```
*Note: If this passes without printing any red "ERROR: AddressSanitizer" messages, your C++ memory management is safe.*

### C. The Code Coverage Report
Use this when you want to see exactly which lines of C++ code our tests are exercising. It recompiles the engine with `gcov` tracking, runs all the tests, and generates interactive HTML reports using `gcovr`.

```bash
# Generate HTML coverage reports
./run_coverage.sh
```
*Note: You can view the results by opening `coverage_reports/cpp/html/index.html` in your web browser. We currently have **84.6% line coverage** and **100% function coverage**!*

---

## 3. Understanding Mutation Testing
We configured `mutmut` in our `pyproject.toml`. Mutation testing answers the question: *"Who tests the tests?"* It works by modifying (mutating) your source code (e.g., changing a `>` to a `<`) and ensuring your tests actually fail. If your tests still pass, it means your tests aren't thorough enough.

**Why aren't we running it yet?**
`mutmut` is designed to mutate *Python* source code. Because DECODE is a C++ engine, we don't actually have any Python application source code right now (the entire logic is compiled into a C++ `.so` extension). When we eventually build Python wrapping logic around the engine, `mutmut` will automatically start mutating it. For true C++ mutation testing, we would use a tool called `mull` which requires switching our compiler from GCC to Clang.
