# Important Files
> **Onboarding question:** Which files should I understand first?

When diving into this codebase, you shouldn't try to read everything at once. The most critical file to understand first is `vis-network.min.js`. It acts as a component—meaning almost every other part of the system interacts with it. Once you understand that, look at `tom-select.complete.min.js`, which serves as a component.


## `./lib/vis-9.1.2/vis-network.min.js`
The file `vis-network.min.js` is crucial because it functions as a component. It has 1616 other components depending on it, and it orchestrates 1517 different downstream tasks.

### Key Symbols

- `Function Nn`

- `Function Fn`

- `Function An`

- `Function jn`

- `Function Rn`


---

## `./lib/tom-select/tom-select.complete.min.js`
The file `tom-select.complete.min.js` is crucial because it functions as a component. It has 3 other components depending on it, and it orchestrates 681 different downstream tasks.

### Key Symbols

- `Function e`

- `Class t`

- `Method constructor`

- `Method on`

- `Method off`


---

## `./.coverage`
The file `.coverage` is crucial because it functions as a component. It has 0 other components depending on it, and it orchestrates 0 different downstream tasks.

### Key Symbols


---

## `./.gitignore`
The file `.gitignore` is crucial because it functions as a component. It has 0 other components depending on it, and it orchestrates 0 different downstream tasks.

### Key Symbols


---

## `./src/python/decode_snapshot/snapshot_generator.py`
The file `snapshot_generator.py` is crucial because it functions as a component. It has 15 other components depending on it, and it orchestrates 209 different downstream tasks.

### Key Symbols

- `Function _sanitize_path`

- `Function _build_project_stats`

- `Function _build_per_file_context`

- `Function update_session_memory`

- `Function generate_xml_bundle`


---

## `./src/python/decode_db/query_api.py`
The file `query_api.py` is crucial because it functions as a api router. It has 0 other components depending on it, and it orchestrates 204 different downstream tasks.

### Key Symbols

- `Class DBQueryAPI`

- `Method __init__`

- `Method find_symbol`

- `Method find_files_importing`

- `Method get_file_outline`


---

## `./src/python/decode_graphs/graph_generator.py`
The file `graph_generator.py` is crucial because it functions as a component. It has 15 other components depending on it, and it orchestrates 87 different downstream tasks.

### Key Symbols

- `Function _create_network`

- `Function _get_file_tooltip`

- `Function _get_symbol_tooltip`

- `Function _get_class_tooltip`

- `Function render_dependency_graph`


---

## `./src/parser/ast_parser.hpp`
The file `ast_parser.hpp` is crucial because it functions as a core dependency. It has 40 other components depending on it, and it orchestrates 0 different downstream tasks.

### Key Symbols

- `Class ASTParser`


---

## `./decode.py`
The file `decode.py` is crucial because it functions as a coordinator. It has 1 other components depending on it, and it orchestrates 45 different downstream tasks.

### Key Symbols

- `Function main`


---

## `./src/core/language_detector.cpp`
The file `language_detector.cpp` is crucial because it functions as a core dependency. It has 21 other components depending on it, and it orchestrates 0 different downstream tasks.

### Key Symbols

- `Function trim_whitespace`

- `Function detect_language`


---

## `./src/run_indexer.py`
The file `run_indexer.py` is crucial because it functions as a coordinator. It has 2 other components depending on it, and it orchestrates 68 different downstream tasks.

### Key Symbols

- `Function run_indexer`


---

## `./src/python/decode_docs/base_generator.py`
The file `base_generator.py` is crucial because it functions as a entry point. It has 0 other components depending on it, and it orchestrates 17 different downstream tasks.

### Key Symbols

- `Class BaseGenerator`

- `Method __init__`

- `Method gather_data`

- `Method should_generate`

- `Method _generate_ai_summary`


---

## `./tests/db/test_manager.py`
The file `test_manager.py` is crucial because it functions as a test suite. It has 0 other components depending on it, and it orchestrates 56 different downstream tasks.

### Key Symbols

- `Function test_schema_setup`

- `Function test_bulk_ingestion`

- `Function test_get_existing_files`

- `Function test_remove_stale_files_cascade`

- `Function test_empty_ingestions`


---

## `./src/python/decode_db/manager.py`
The file `manager.py` is crucial because it functions as a orchestrator. It has 0 other components depending on it, and it orchestrates 39 different downstream tasks.

### Key Symbols

- `Function set_sqlite_pragma`

- `Class DBManager`

- `Method __init__`

- `Method get_existing_files`

- `Method remove_stale_files`


---

## `./tests/core/test_core_stress.py`
The file `test_core_stress.py` is crucial because it functions as a test suite. It has 0 other components depending on it, and it orchestrates 55 different downstream tasks.

### Key Symbols

- `Function test_negative_invalid_types`

- `Function test_large_file_ast_stress`

- `Function test_walker_concurrency_race`

- `Function file_mutator`


---

## `./lib/bindings/utils.js`
The file `utils.js` is crucial because it functions as a utility library. It has 5 other components depending on it, and it orchestrates 31 different downstream tasks.

### Key Symbols

- `Function neighbourhoodHighlight`

- `Function filterHighlight`

- `Function selectNode`

- `Function selectNodes`

- `Function highlightFilter`


---

## `./src/parser/symbol_extractor.cpp`
The file `symbol_extractor.cpp` is crucial because it functions as a core dependency. It has 15 other components depending on it, and it orchestrates 0 different downstream tasks.

### Key Symbols

- `Function extract_text`


---

## `./tests/parser/test_inheritance.py`
The file `test_inheritance.py` is crucial because it functions as a test suite. It has 0 other components depending on it, and it orchestrates 28 different downstream tasks.

### Key Symbols

- `Class TestPythonInheritance`

- `Method _parse`

- `Method test_single_inheritance_detected`

- `Method test_inheritance_caller_is_child_class`

- `Method test_multiple_inheritance`


---

## `./tests/parser/test_return_types.py`
The file `test_return_types.py` is crucial because it functions as a test suite. It has 0 other components depending on it, and it orchestrates 19 different downstream tasks.

### Key Symbols

- `Class TestPythonReturnTypes`

- `Method _parse`

- `Method test_simple_type_annotation`

- `Method test_none_return_annotation`

- `Method test_generic_return_annotation`


---

## `./src/core/fs_walker.cpp`
The file `fs_walker.cpp` is crucial because it functions as a core dependency. It has 10 other components depending on it, and it orchestrates 0 different downstream tasks.

### Key Symbols

- `Function should_skip`

- `Function walk_repository`


---


*Generated by DECODE NLG | [← Back to Index](index.md)*