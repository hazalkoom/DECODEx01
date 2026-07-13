# Architecture Upgrade: DECODE C++ AST Engine (Path C)

## Overview
Upgraded the core Tree-sitter C++ parsing engine from a basic file-level import scanner into a deep, semantic **Single-Pass Call Graph Engine**. The engine now extracts function/method calls, object instantiations, full signatures, and documentation strings in a single, highly-optimized pass.

## Core Achievements

### 1. Data Model Overhaul (`ast_types.hpp`)
*   **Strong Typing:** Introduced `SymbolKind` and `ReferenceKind` enums for type safety (replacing raw strings).
*   **Deep Context:** Upgraded the `Symbol` struct to capture `fully_qualified_name`, `signature`, `return_type`, and `docstring` (to save AI context tokens).
*   **Call Graphing:** Created a `Reference` struct containing `caller_fqn` and `callee_fqn` to track exactly which function invokes another.
*   **Single-Pass Payload:** Wrapped all outputs into a master `FileContext` struct.

### 2. Single-Pass Parsing Engine (`ast_parser.cpp`)
*   Replaced the redundant `extract_symbols` and `extract_dependencies` methods with a unified `analyze_file()` method.
*   The engine now parses the source code into an AST exactly **once**, applying all Tree-sitter queries simultaneously, vastly improving CPU efficiency.
*   Added `reference_query_str` configurations for all 8 supported languages (Python, C++, JS, Go, Rust, etc.).

### 3. Context-Aware Extractors
*   **`reference_extractor.cpp`:** Implemented logic to walk *up* the AST from a function call to determine the enclosing parent scope (`caller_fqn`), creating an unbreakable link between caller and callee.
*   **`symbol_extractor.cpp`:** Added backward-scanning logic to extract preceding comments/docstrings and upward-scanning logic to build fully qualified paths (e.g., `Database::connect`).

### 4. Bridge & Integration
*   **`bindings.cpp`:** Exposed the new Enums, `Reference`, and `FileContext` structs to Python via pybind11.
*   **`CMakeLists.txt`:** Registered `reference_extractor.cpp` in the build target.
*   **`run_indexer.py`:** Updated the Python SQLite orchestrator to consume the new `parser.analyze_file()` output and package `refs_data` for database ingestion.