# Phase 1 Report: Heuristic-Based Setup Guide Generation
**Date:** 2026-07-14
**Status:** ✅ Complete

## Overview
We successfully implemented Phase 1 of the NLG Engine V2 Upgrade: generating a highly accurate `SETUP.md` document purely by scanning root configuration files—without using any AI, LLMs, or external APIs.

## Implementation Details

### 1. Root Scanner Heuristics (`decode_docs/nlg/scanners/root_scanner.py`)
We built a heuristic engine that directly inspects the project's root folder for standard configuration files (`pyproject.toml`, `package.json`, `CMakeLists.txt`, `docker-compose.yml`, etc.).
- Using a built-in `CONFIG_KNOWLEDGE_BASE`, it maps detected files to natural-language prerequisites (e.g., "Python 3.10+ and Poetry 1.8+") and standard shell installation steps (e.g., `poetry install`).
- It parses `pyproject.toml` and `package.json` to extract the `name` and `description`.
- It dynamically reads the first non-header line of the `README.md` to establish the core "Project Purpose" statement.

### 2. Generator & Template
- Added a `SetupGuideGenerator` that executes the scanner during the `gather_data()` phase.
- Added `setup.md.jinja2`, which iterates over the heuristically derived prerequisites and commands, wrapping them in clean Markdown bash blocks.
- Wired the generator into `DocsCoordinator` and passed the `project_root` parameter from `decode.py`.

## Verification
-   **Tests Updated:** `tests/docs/test_docs_generator.py` now explicitly verifies that a 12th document, `SETUP.md`, is outputted.
-   **Output Quality:** Running `decode docs` on DECODE's own repository perfectly detected both `pyproject.toml` and `CMakeLists.txt`, outputting instructions to run `poetry install` and `cmake .. && make`. It also successfully extracted the project purpose from `README.md`: *"The operating system for understanding code."*
