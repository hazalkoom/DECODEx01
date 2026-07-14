# Call Flow
> **Onboarding question:** What happens during execution?


## Flow from `main`

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `lstrip`, `exists`, and `connect`.

```mermaid
sequenceDiagram
    participant Start as main


    main->>ArgumentParser: calls



    main->>add_subparsers: calls



    main->>add_parser: calls



    main->>add_argument: calls



    main->>add_parser: calls



    main->>add_argument: calls



    main->>add_parser: calls



    main->>add_argument: calls



    main->>add_argument: calls



    main->>add_argument: calls



    main->>add_parser: calls



    main->>add_argument: calls



    main->>add_argument: calls



    main->>add_parser: calls



    main->>add_argument: calls



    main->>add_argument: calls



    main->>add_argument: calls



    main->>add_argument: calls



    main->>add_parser: calls



    main->>add_argument: calls


```

## Flow from `TestCppInheritance.test_cpp_function_calls_remain_call_kind`

The `test_cpp_function_calls_remain_call_kind` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 2 different components. The primary interactions involve `_parse` and `len`.

```mermaid
sequenceDiagram
    participant Start as TestCppInheritance_test_cpp_function_calls_remain_call_kind


    TestCppInheritance_test_cpp_function_calls_remain_call_kind->>_parse: calls



    TestCppInheritance_test_cpp_function_calls_remain_call_kind->>len: calls


```

## Flow from `DBQueryAPI.get_domain_entities`

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `join`, `query`, and `SessionLocal`.

```mermaid
sequenceDiagram
    participant Start as DBQueryAPI_get_domain_entities


    DBQueryAPI_get_domain_entities->>SessionLocal: calls



    DBQueryAPI_get_domain_entities->>query: calls



    DBQueryAPI_get_domain_entities->>join: calls



    DBQueryAPI_get_domain_entities->>filter: calls



    DBQueryAPI_get_domain_entities->>all: calls



    DBQueryAPI_get_domain_entities->>defaultdict: calls



    DBQueryAPI_get_domain_entities->>query: calls



    DBQueryAPI_get_domain_entities->>all: calls



    DBQueryAPI_get_domain_entities->>any: calls



    DBQueryAPI_get_domain_entities->>query: calls



    DBQueryAPI_get_domain_entities->>filter: calls



    DBQueryAPI_get_domain_entities->>in_: calls



    DBQueryAPI_get_domain_entities->>count: calls



    DBQueryAPI_get_domain_entities->>append: calls



    DBQueryAPI_get_domain_entities->>sort: calls


```

## Flow from `J.onClick`

The `onClick` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `blur`, `focus`, and `clearActiveItems`.

```mermaid
sequenceDiagram
    participant Start as J_onClick


    J_onClick->>clearActiveItems: calls



    J_onClick->>focus: calls



    J_onClick->>blur: calls



    J_onClick->>focus: calls


```

## Flow from `J.setup`

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 58 different components. The primary interactions involve `create`, `updateOriginalInput`, and `P`.

```mermaid
sequenceDiagram
    participant Start as J_setup


    J_setup->>P: calls



    J_setup->>P: calls



    J_setup->>M: calls



    J_setup->>replace: calls



    J_setup->>querySelector: calls



    J_setup->>bind: calls



    J_setup->>B: calls



    J_setup->>P: calls



    J_setup->>M: calls



    J_setup->>P: calls



    J_setup->>P: calls



    J_setup->>join: calls



    J_setup->>C: calls



    J_setup->>P: calls



    J_setup->>P: calls



    J_setup->>v: calls



    J_setup->>z: calls



    J_setup->>B: calls



    J_setup->>k: calls



    J_setup->>onOptionSelect: calls


```

## Flow from `J.setupOptions`

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `addOptions`, `y`, and `registerOptionGroup`.

```mermaid
sequenceDiagram
    participant Start as J_setupOptions


    J_setupOptions->>addOptions: calls



    J_setupOptions->>y: calls



    J_setupOptions->>registerOptionGroup: calls


```

## Flow from `J.setupTemplates`

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 77 different components. The primary interactions involve `set`, `Kp`, and `call`.

```mermaid
sequenceDiagram
    participant Start as J_setupTemplates


    J_setupTemplates->>createElement: calls



    J_setupTemplates->>appendChild: calls



    J_setupTemplates->>t: calls



    J_setupTemplates->>i: calls



    J_setupTemplates->>i: calls



    J_setupTemplates->>t: calls



    J_setupTemplates->>assign: calls



    t->>set: calls



    t->>vg: calls



    t->>handler: calls



    t->>init: calls



    t->>Rv: calls



    t->>qv: calls



    t->>py: calls



    t->>pg: calls



    t->>add: calls



    t->>recognizeWith: calls



    t->>requireFailure: calls



    t->>Yd: calls



    t->>_create: calls


```

## Flow from `J.setupCallbacks`

The `setupCallbacks` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `on`.

```mermaid
sequenceDiagram
    participant Start as J_setupCallbacks


    J_setupCallbacks->>on: calls


```

## Flow from `test_schema_setup`

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `SessionLocal`, `execute`, and `len`.

```mermaid
sequenceDiagram
    participant Start as test_schema_setup


    test_schema_setup->>SessionLocal: calls



    test_schema_setup->>execute: calls



    test_schema_setup->>select: calls



    test_schema_setup->>all: calls



    test_schema_setup->>execute: calls



    test_schema_setup->>select: calls



    test_schema_setup->>all: calls



    test_schema_setup->>execute: calls



    test_schema_setup->>select: calls



    test_schema_setup->>all: calls



    test_schema_setup->>execute: calls



    test_schema_setup->>select: calls



    test_schema_setup->>all: calls



    test_schema_setup->>len: calls



    test_schema_setup->>len: calls



    test_schema_setup->>len: calls



    test_schema_setup->>len: calls


```

## Flow from `J.registerOption`

The `registerOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `addOption`.

```mermaid
sequenceDiagram
    participant Start as J_registerOption


    J_registerOption->>addOption: calls


```

## Flow from `J.registerOptionGroup`

The `registerOptionGroup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `q`.

```mermaid
sequenceDiagram
    participant Start as J_registerOptionGroup


    J_registerOptionGroup->>q: calls


```

## Flow from `ArchitectureGenerator.gather_data`

The `gather_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `architecture.py`. From there, it coordinates with 2 different components. The primary interactions involve `get_module_structure` and `get_cross_module_edges`.

```mermaid
sequenceDiagram
    participant Start as ArchitectureGenerator_gather_data


    ArchitectureGenerator_gather_data->>get_module_structure: calls



    ArchitectureGenerator_gather_data->>get_cross_module_edges: calls


```

## Flow from `BaseGenerator._generate_ai_summary`

The `_generate_ai_summary` workflow represents a critical path in the system. When this flow is triggered, execution begins in `base_generator.py`. From there, it coordinates with 6 different components. The primary interactions involve `create`, `strip`, and `dumps`.

```mermaid
sequenceDiagram
    participant Start as BaseGenerator__generate_ai_summary


    BaseGenerator__generate_ai_summary->>getenv: calls



    BaseGenerator__generate_ai_summary->>print: calls



    BaseGenerator__generate_ai_summary->>getenv: calls



    BaseGenerator__generate_ai_summary->>OpenAI: calls



    BaseGenerator__generate_ai_summary->>print: calls



    BaseGenerator__generate_ai_summary->>create: calls



    BaseGenerator__generate_ai_summary->>dumps: calls



    BaseGenerator__generate_ai_summary->>strip: calls



    BaseGenerator__generate_ai_summary->>print: calls


```

## Flow from `DocsCoordinator.generate_all`

The `generate_all` workflow represents a critical path in the system. When this flow is triggered, execution begins in `coordinator.py`. From there, it coordinates with 3 different components. The primary interactions involve `generate`, `makedirs`, and `_render_index`.

```mermaid
sequenceDiagram
    participant Start as DocsCoordinator_generate_all


    DocsCoordinator_generate_all->>makedirs: calls



    DocsCoordinator_generate_all->>generate: calls



    DocsCoordinator_generate_all->>_render_index: calls


```

## Flow from `Ey`

The `Ey` workflow represents a critical path in the system. When this flow is triggered, execution begins in `vis-network.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `create` and `qv`.

```mermaid
sequenceDiagram
    participant Start as Ey


    Ey->>create: calls



    Ey->>qv: calls


```

## Flow from `J.addOption`

The `addOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `q`, `trigger`, and `addOptions`.

```mermaid
sequenceDiagram
    participant Start as J_addOption


    J_addOption->>isArray: calls



    J_addOption->>addOptions: calls



    J_addOption->>q: calls



    J_addOption->>hasOwnProperty: calls



    J_addOption->>trigger: calls


```

## Flow from `J.advanceSelection`

The `advanceSelection` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 8 different components. The primary interactions involve `getLastActive`, `K`, and `setActiveItemClass`.

```mermaid
sequenceDiagram
    participant Start as J_advanceSelection


    J_advanceSelection->>inputValue: calls



    J_advanceSelection->>K: calls



    J_advanceSelection->>K: calls



    J_advanceSelection->>getLastActive: calls



    J_advanceSelection->>contains: calls



    J_advanceSelection->>getAdjacent: calls



    J_advanceSelection->>contains: calls



    J_advanceSelection->>removeActiveItem: calls



    J_advanceSelection->>setActiveItemClass: calls



    J_advanceSelection->>moveCaret: calls


```

## Flow from `J.clearOptions`

The `clearOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `trigger`, `y`, and `clearCache`.

```mermaid
sequenceDiagram
    participant Start as J_clearOptions


    J_clearOptions->>clearCache: calls



    J_clearOptions->>y: calls



    J_clearOptions->>indexOf: calls



    J_clearOptions->>trigger: calls


```

## Flow from `J.getScoreFunction`

The `getScoreFunction` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `getSearchOptions` and `getScoreFunction`.

```mermaid
sequenceDiagram
    participant Start as J_getScoreFunction


    J_getScoreFunction->>getScoreFunction: calls



    J_getScoreFunction->>getSearchOptions: calls


```

## Flow from `TestPythonInheritance.test_single_inheritance_detected`

The `test_single_inheritance_detected` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 3 different components. The primary interactions involve `dedent`, `_parse`, and `len`.

```mermaid
sequenceDiagram
    participant Start as TestPythonInheritance_test_single_inheritance_detected


    TestPythonInheritance_test_single_inheritance_detected->>dedent: calls



    TestPythonInheritance_test_single_inheritance_detected->>_parse: calls



    TestPythonInheritance_test_single_inheritance_detected->>len: calls


```

## Flow from `language_repo`

The `language_repo` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_language_detector.py`. From there, it coordinates with 2 different components. The primary interactions involve `write_text` and `str`.

```mermaid
sequenceDiagram
    participant Start as language_repo


    language_repo->>write_text: calls



    language_repo->>write_text: calls



    language_repo->>write_text: calls



    language_repo->>write_text: calls



    language_repo->>write_text: calls



    language_repo->>write_text: calls



    language_repo->>str: calls



    language_repo->>str: calls



    language_repo->>str: calls



    language_repo->>str: calls



    language_repo->>str: calls



    language_repo->>str: calls


```

## Flow from `test_find_symbol_missing`

The `test_find_symbol_missing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api.py`. From there, it coordinates with 3 different components. The primary interactions involve `find_symbol`, `isinstance`, and `len`.

```mermaid
sequenceDiagram
    participant Start as test_find_symbol_missing


    test_find_symbol_missing->>find_symbol: calls



    test_find_symbol_missing->>isinstance: calls



    test_find_symbol_missing->>len: calls


```

## Flow from `test_get_existing_files`

The `test_get_existing_files` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 3 different components. The primary interactions involve `len`, `isinstance`, and `get_existing_files`.

```mermaid
sequenceDiagram
    participant Start as test_get_existing_files


    test_get_existing_files->>get_existing_files: calls



    test_get_existing_files->>isinstance: calls



    test_get_existing_files->>len: calls


```

## Flow from `test_language_detection`

The `test_language_detection` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_language_detector.py`. From there, it coordinates with 1 different components. The primary interactions involve `detect_language`.

```mermaid
sequenceDiagram
    participant Start as test_language_detection


    test_language_detection->>detect_language: calls



    test_language_detection->>detect_language: calls



    test_language_detection->>detect_language: calls



    test_language_detection->>detect_language: calls



    test_language_detection->>detect_language: calls



    test_language_detection->>detect_language: calls


```

## Flow from `test_python_garbage_safety`

The `test_python_garbage_safety` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_ast_parser.py`. From there, it coordinates with 6 different components. The primary interactions involve `isinstance`, `dedent`, and `ASTParser`.

```mermaid
sequenceDiagram
    participant Start as test_python_garbage_safety


    test_python_garbage_safety->>ASTParser: calls



    test_python_garbage_safety->>set_language: calls



    test_python_garbage_safety->>dedent: calls



    test_python_garbage_safety->>extract_symbols: calls



    test_python_garbage_safety->>extract_dependencies: calls



    test_python_garbage_safety->>isinstance: calls



    test_python_garbage_safety->>isinstance: calls


```

## Flow from `test_walker_nonexistent_directory`

The `test_walker_nonexistent_directory` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_fs_walker.py`. From there, it coordinates with 2 different components. The primary interactions involve `walk_repository` and `len`.

```mermaid
sequenceDiagram
    participant Start as test_walker_nonexistent_directory


    test_walker_nonexistent_directory->>walk_repository: calls



    test_walker_nonexistent_directory->>len: calls


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*