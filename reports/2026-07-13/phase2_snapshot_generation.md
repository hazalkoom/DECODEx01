# Phase 2 Report: `decode snapshot` Generation

**Status:** ✅ COMPLETE — **87 tests passed, 0 failed**

---

## What Was Built

The **`decode snapshot`** command was fully implemented to generate an AI-friendly, token-efficient representation of the codebase. Instead of forcing AI agents to read raw source files, they can now read the `SNAPSHOT.md` and structured JSON context files.

### 1. New Module: `decode_snapshot`

Created `src/python/decode_snapshot/snapshot_generator.py` which contains the core generation logic:
- Connects to the existing SQLite `decode_graph.db` using SQLAlchemy.
- Extracts project-wide statistics (total files, classes, functions, references).
- Builds a `SNAPSHOT.md` file acting as the entry point and high-level architectural summary.
- Generates a `.decode/context/` directory with a dedicated JSON file for every indexed source file, containing all Symbols, Imports, and Reference (Call Graph) data.

### 2. CLI Integration

Updated the main entry point `decode.py`:
- Added the `snapshot` subcommand to `argparse`.
- Added the necessary routing logic to trigger `generate_snapshot()`.
- **Fix:** Fixed Python import path issues (`sys.path`) so that the root `decode.py` script and the `pytest` environment both successfully resolve `src/` modules.

### 3. File Structure of the Snapshot

Running `poetry run python decode.py snapshot` successfully produces the following structure:
```text
.decode/
├── SNAPSHOT.md                  # High-level overview, stats, and module index
└── context/                     # JSON files per source file
    ├── src_python_decode_db_schema.py.json
    ├── scripts_run_indexer.py.json
    └── ...
```

---

## Files Created & Modified

### Created
| File | Purpose |
|------|---------|
| `src/python/decode_snapshot/__init__.py` | Module initialization |
| `src/python/decode_snapshot/snapshot_generator.py` | Core DB extraction and `.decode/` file generation |
| `tests/snapshot/test_snapshot_generator.py` | Pytest suite for snapshot logic using `conftest.py` fixtures |

### Modified
| File | Purpose |
|------|---------|
| `decode.py` | Added the `snapshot` command and fixed `sys.path` for robust imports |
| `tests/parser/test_parser_fuzz.py` | Fixed a false-positive in the fuzz test where Hypothesis legitimately generated the valid string `"cpp"` |
| `tests/conftest.py` | Relocated from `tests/db/conftest.py` to `tests/conftest.py` to share DB fixtures across both `db/` and `snapshot/` test directories |

---

## Test Results

A new `test_snapshot_generation` test was added to verify:
1. The `.decode/` directory and `SNAPSHOT.md` are correctly generated.
2. The `context/` directory contains the correct number of JSON files.
3. The content of the JSON files perfectly matches the expected AST symbols, imports, and calls.

```text
============================= test session starts ==============================
...
tests/snapshot/test_snapshot_generator.py::test_snapshot_generation PASSED [100%]

============================== 87 passed in 7.83s ==============================
```

All 87 tests in the project are passing successfully with 0 failures.

---

**⏸️ Phase 2 halted. Awaiting your explicit approval to begin Phase 3 (`decode docs` and graph upgrades).**
