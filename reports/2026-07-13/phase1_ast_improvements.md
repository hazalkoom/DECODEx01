# Phase 1 Report: AST Engine Improvements

**Status:** ✅ COMPLETE — **86 tests passed, 0 failed**

---

## What Was Changed

### C++ Layer

#### `src/parser/symbol_extractor.hpp` + `symbol_extractor.cpp`
**What:** Added `extract_return_type()` helper — replaces the old hardcoded `"auto"` fallback.

**How it works:**
- **Python:** Reads the `return_type` field of the `function_definition` AST node (e.g. `-> int` in `def foo() -> int`), strips the `->` arrow, and returns the clean type string.
- **C++:** Walks up from the `function_declarator` to the `function_definition` and reads its `type` field (e.g. `int` in `int foo() {}`).
- **Classes:** Return type is set to `""` (empty) — classes don't have return types.
- **Unannotated functions:** Falls back to `"auto"` as before.

#### `src/parser/ast_parser.cpp`
**What:** Added two new Tree-sitter capture queries for inheritance detection.

| Language | Query Added |
|----------|------------|
| Python | `(class_definition (argument_list (identifier) @callee_name))` |
| C++ | `(base_class_clause (type_identifier) @callee_name)` |

> **Debugging note:** The initial plan used `base_class_specifier` as the node name, but
> the installed version of tree-sitter-cpp uses `base_class_clause` directly containing
> `type_identifier` (no intermediate specifier wrapper). This was verified by reading
> the grammar's `grammar.json` file.

#### `src/parser/reference_extractor.cpp`
Two improvements:

1. **`determine_caller_fqn()`** — Added a new check: if the reference appears inside a
   `class_definition` / `class_specifier` body (but NOT inside a method), the enclosing
   class name is returned as the caller. This correctly sets `caller_fqn = "Dog"` for
   `class Dog : public Animal` instead of `"<global>"`.

2. **`extract()` loop** — Added `ReferenceKind` detection. If the captured node's parent is
   `base_class_clause` (C++) or `argument_list` within a `class_definition` (Python), the
   reference kind is set to `ReferenceKind::Inheritance` instead of `ReferenceKind::Call`.

### Python Layer

#### `src/python/decode_db/query_api.py`
Added `ReferenceRecord` to imports and three new public methods:

| Method | Description |
|--------|-------------|
| `find_callers_of(symbol_name)` | Reverse call graph: who calls this symbol? |
| `find_calls_by(symbol_name)` | Forward call graph: what does this symbol call? |
| `get_class_hierarchy()` | All `Inheritance` kind references project-wide |

Both `find_callers_of` and `find_calls_by` filter on `kind == "Call"` to exclude inheritance
relationships from call-graph queries.

#### `tests/db/conftest.py`
Extended `populated_db` fixture with 2 additional reference records:
- `utils.helper_func → os.path.join` (Call, file_id=2)
- `AppServer → BaseServer` (Inheritance, file_id=1)

#### `tests/db/test_manager.py`
Updated `test_remove_stale_files_cascade` reference counts to match the new fixture (3 total → 1 remaining after file_id=1 deletion).

---

## New Test Files Created

| File | Tests | Coverage |
|------|-------|----------|
| `tests/parser/test_return_types.py` | 11 | Python annotations, C++ return types, class edge case, unannotated fallback |
| `tests/parser/test_inheritance.py` | 8 | Python single/multiple inheritance, C++ inheritance, caller_fqn correctness, no false positives |
| `tests/db/test_query_api_references.py` | 9 | find_callers_of, find_calls_by, get_class_hierarchy, empty DB, kind filtering |

---

## Test Results

```
============================= 86 passed in 9.33s ==============================
```

| Test Group | Before Phase 1 | After Phase 1 |
|------------|---------------|--------------|
| `tests/core/` | 8 ✅ | 8 ✅ |
| `tests/db/` | 12 ✅ | 21 ✅ (+9 new) |
| `tests/integration/` | 2 ✅ | 2 ✅ |
| `tests/parser/` | 36 ✅ | 55 ✅ (+19 new) |
| **Total** | **58** | **86** |

---

## Data Improvements (What AI Now Gets)

### Before Phase 1
```
def get_user(user_id: int) -> Optional[User]:
    ...
```
```json
{"name": "get_user", "return_type": "auto"}
```

### After Phase 1
```json
{"name": "get_user", "return_type": "Optional[User]"}
```

### Before Phase 1
```python
class AdminUser(BaseUser):
    pass
```
- Inheritance: captured as `ReferenceKind::Call` with `caller_fqn = "<global>"`

### After Phase 1
- Inheritance: captured as `ReferenceKind::Inheritance` with `caller_fqn = "AdminUser"`
- Queryable via `db_query.get_class_hierarchy()`
