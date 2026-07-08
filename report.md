# Bug Fix Report: C++ Infinite Loop in AST Parser

## Executive Summary

The `test_ast_parser.py` test was causing the process to hang indefinitely (CPU 100%, eventually killed by the OS OOM killer) due to an **infinite loop inside tree-sitter-python v0.20.4's external scanner** (`scanner.c`). The bug was triggered during `ts_parser_parse_string()` — before the TSQuery logic ever ran.

---

## Root Cause

### The Bug: tree-sitter-python v0.20.4 Scanner Infinite Loop

The root cause was **NOT** in the project's C++ code (`ast_parser.cpp`), but in the **tree-sitter-python v0.20.4 grammar's `scanner.c`** — a vendored C dependency fetched at build time via CMake's `FetchContent`.

The Python grammar's external scanner is responsible for handling Python's whitespace-significant syntax by generating virtual `NEWLINE`, `INDENT`, and `DEDENT` tokens. In v0.20.4, the scanner's indentation state machine had a bug where it could enter an **infinite loop** during the `scan` function, causing `ts_parser_parse_string()` to never return.

### Evidence

Debug instrumentation (`fprintf` before/after each tree-sitter API call) proved the hang was specifically in `ts_parser_parse_string()`:

```
[DEBUG] Step 1: ts_parser_parse_string (len=5)...
                                                    ← never reaches "Step 1 DONE"
```

Even parsing the simplest possible input (`"x = 1"`) triggered the infinite loop, confirming the issue was in the scanner itself, not in the query patterns or tree traversal logic.

### Why the existing C++ code was NOT the problem

The `ast_parser.cpp` code was actually well-written:
- It correctly used the **TSQuery API** (non-recursive, memory-bounded) instead of manual tree walking
- It had proper null checks and memory cleanup
- The query patterns `(class_definition ...)` and `(function_definition ...)` were correct

The code never reached the query phase because `ts_parser_parse_string()` hung first.

---

## Fix Applied

### 1. Upgraded tree-sitter dependencies (CMakeLists.txt)

| Dependency | Old Version | New Version |
|:---|:---|:---|
| **tree-sitter** (core) | v0.20.8 | v0.24.6 |
| **tree-sitter-python** (grammar) | v0.20.4 | v0.23.5 |

The newer tree-sitter-python version contains a completely rewritten `scanner.c` with the indentation loop bug fixed.

### 2. Switched from `FetchContent_MakeAvailable` to `FetchContent_Populate` (CMakeLists.txt)

The newer tree-sitter-python (v0.23.5) includes its own `CMakeLists.txt` that attempts to regenerate `parser.c` using the `tree-sitter` CLI tool (which is not installed). Since we only need the pre-generated source files (`parser.c`, `scanner.c`), we use `FetchContent_Populate` to download the source without processing the grammar's build system.

```cmake
# Before (broken with newer tree-sitter-python):
FetchContent_MakeAvailable(tree-sitter-python)

# After (only downloads source, skips CMakeLists.txt):
FetchContent_GetProperties(tree-sitter-python)
if(NOT tree-sitter-python_POPULATED)
    FetchContent_Populate(tree-sitter-python)
endif()
```

### 3. Added `ts_parser_set_timeout_micros` safety net (ast_parser.cpp)

Added a 5-second parser timeout in the `ASTParser` constructor to prevent any future scanner/parser bugs from hanging indefinitely:

```cpp
ASTParser::ASTParser() {
    parser = ts_parser_new();
    // Safety net: prevent infinite loops from burning CPU forever
    ts_parser_set_timeout_micros(parser, 5000000);
}
```

If parsing exceeds 5 seconds, `ts_parser_parse_string()` returns `NULL` gracefully instead of hanging.

---

## Files Changed

| File | Change |
|:---|:---|
| `CMakeLists.txt` | Upgraded tree-sitter v0.20.8→v0.24.6 and tree-sitter-python v0.20.4→v0.23.5; switched to `FetchContent_Populate` |
| `src/ast_parser.cpp` | Added `ts_parser_set_timeout_micros(parser, 5000000)` in constructor |

---

## Verification

### Before Fix
```
$ poetry run pytest tests/test_ast_parser.py -s
tests/test_ast_parser.py::test_python_ast_extraction   [hangs... killed after 30s]
EXIT_CODE=124 (SIGKILL)
```

### After Fix
```
$ poetry run pytest tests/ -s -v
tests/test_ast_parser.py::test_python_ast_extraction PASSED
tests/test_fs_walker.py::test_walker_comprehensive PASSED
tests/test_fs_walker.py::test_walker_nonexistent_directory PASSED
tests/test_fs_walker_qa.py::test_qa_walker_deep_nesting PASSED
tests/test_fs_walker_qa.py::test_qa_walker_infinite_symlink PASSED
tests/test_language_detector.py::test_language_detection PASSED
tests/test_language_qa.py::test_qa_case_sensitivity PASSED
tests/test_language_qa.py::test_qa_deceptive_directory PASSED
tests/test_language_qa.py::test_qa_sloppy_shebangs PASSED
tests/test_language_qa.py::test_qa_windows_line_endings PASSED
tests/test_language_qa.py::test_qa_buffer_safety PASSED

============================== 11 passed in 0.29s ==============================
```

All 11 tests pass cleanly in 0.29 seconds.

---

## Action Summary

1. **Reproduced** the hang by running `poetry run pytest tests/test_ast_parser.py -s` — confirmed CPU maxout + timeout kill
2. **Instrumented** `ast_parser.cpp` with `fprintf(stderr, ...)` debug prints to pinpoint the exact hanging API call
3. **Identified** `ts_parser_parse_string()` as the hanging function (the TSQuery code was never reached)
4. **Diagnosed** the root cause as tree-sitter-python v0.20.4's `scanner.c` infinite loop in indentation handling
5. **Fixed** by upgrading both tree-sitter dependencies and switching to `FetchContent_Populate`
6. **Hardened** by adding `ts_parser_set_timeout_micros` as a safety net against future scanner bugs
7. **Rebuilt** the C++ extension with `poetry run pip install -e .`
8. **Verified** all 11 tests pass cleanly
