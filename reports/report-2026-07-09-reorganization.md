# Source Code Reorganization Report

## Date: July 9, 2026

## Overview
We successfully reorganized the `src/` directory to adhere to the Single Responsibility architecture philosophy ("Organize by responsibility/feature, not file type"). The flat structure has been replaced with a logical modular layout.

## New Folder Structure
The C++ source files have been categorized into three main components:

1. **`src/core/`**: Shared code and foundational utilities.
   - `ast_types.hpp`
   - `fs_walker.cpp` / `fs_walker.hpp`
   - `language_detector.cpp` / `language_detector.hpp`

2. **`src/parser/`**: The core Tree-sitter routing logic and specific extractors.
   - `ast_parser.cpp` / `ast_parser.hpp`
   - `symbol_extractor.cpp` / `symbol_extractor.hpp`
   - `dependency_extractor.cpp` / `dependency_extractor.hpp`

3. **`src/api/`**: The `pybind11` integration layer.
   - `bindings.cpp`

## Changes Made
- Executed `git mv` to move all `.cpp` and `.hpp` files into their respective subdirectories to preserve git history.
- Updated `#include` directives in `ast_parser.hpp`, `symbol_extractor.hpp`, `dependency_extractor.hpp`, and `bindings.cpp` to correctly reference headers using relative paths (e.g., `#include "../core/ast_types.hpp"`).
- Adjusted `CMakeLists.txt` to point to the new paths in `pybind11_add_module`.
- Added the new `core/`, `parser/`, and `api/` directories to `target_include_directories` in `CMakeLists.txt` for robust resolution.

## Build and Testing Verification
- Ran `./dev-install.sh` to compile the C++ extension. The build completed **successfully** with the persistent cache `scikit-build-core` flow.
- Ran `poetry run pytest tests/` to verify functionality. All **13 tests passed successfully**, confirming the reorganization did not introduce any breaking changes.
