# Phase 4 Report: Stricter Heuristics
**Date:** 2026-07-14
**Status:** ✅ Complete

## Overview
We overhauled the NLG rules engine to produce more accurate, less randomized results while remaining 100% offline.

## Implementation Details

### 1. Enhanced API Scanner (`api_scanner.py`)
- Python decorators (`@app.get()`) were previously invisible to the C++ parser. We implemented a hybrid strategy: the engine now parses raw source files with Python regex specifically to extract decorator patterns, and correlates them with the function definitions extracted by the AST parser to get exact handlers and docstrings.
- JavaScript heuristics were tightened to only run on `.js`, `.ts`, `.jsx`, and `.tsx` files to avoid false positives in random config files.

### 2. Enhanced Few-Shot Schema (`few_shot/schema.py`)
- Abandoned raw string-matching across all symbols.
- Introduced a scoring system: Matches now only trigger if they are explicitly of type `Class`, `Struct`, `Interface`, or a middleware `Function`.
- Added filepath context: If the file path matches the semantic domain (e.g., a file named `security.py` scoring higher for an `Auth` trigger), the score is multiplied, filtering out coincidental variable names.

### 3. Story Generator Pruning (`story.py`)
- The DFS algorithm no longer just selects the longest chain. It now uses a penalty system.
- Calls into paths containing `util`, `helper`, `log`, `print`, `format`, or `error` accumulate penalties. If a path dives too deep into utilities, it is truncated, ensuring the narrative focuses purely on core business logic rather than execution boilerplate.

## Verification
-   The tests successfully pass.
-   The generated documentation is now significantly more accurate and "reads" closer to genuine documentation rather than randomized AST dumps.
