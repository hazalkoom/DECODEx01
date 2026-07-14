# Call Flow
> **Onboarding question:** What happens during execution?


## Flow from `main`

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `connect`, `FileSystemLoader`, and `execute`.

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

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `filter`, `query`, and `count`.

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

The `onClick` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `clearActiveItems`, `blur`, and `focus`.

```mermaid
sequenceDiagram
    participant Start as J_onClick


    J_onClick->>clearActiveItems: calls



    J_onClick->>focus: calls



    J_onClick->>blur: calls



    J_onClick->>focus: calls


```

## Flow from `J.setup`

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 58 different components. The primary interactions involve `close`, `M`, and `h`.

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

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `registerOptionGroup`, `addOptions`, and `y`.

```mermaid
sequenceDiagram
    participant Start as J_setupOptions


    J_setupOptions->>addOptions: calls



    J_setupOptions->>y: calls



    J_setupOptions->>registerOptionGroup: calls


```

## Flow from `J.setupTemplates`

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 77 different components. The primary interactions involve `setImages`, `py`, and `Kv`.

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



    i->>off: calls



    i->>apply: calls



    i->>d: calls



    i->>call: calls



    i->>resolve: calls



    i->>then: calls



    i->>i: calls



    i->>i: calls



    i->>resolve: calls



    i->>then: calls



    i->>s: calls



    i->>i: calls



    i->>a: calls


```

## Flow from `J.setupCallbacks`

The `setupCallbacks` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `on`.

```mermaid
sequenceDiagram
    participant Start as J_setupCallbacks


    J_setupCallbacks->>on: calls


```

## Flow from `test_schema_setup`

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `execute`, `select`, and `SessionLocal`.

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

## Flow from `DBManager.remove_stale_files`

The `remove_stale_files` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 9 different components. The primary interactions involve `range`, `in_`, and `rollback`.

```mermaid
sequenceDiagram
    participant Start as DBManager_remove_stale_files


    DBManager_remove_stale_files->>SessionLocal: calls



    DBManager_remove_stale_files->>range: calls



    DBManager_remove_stale_files->>len: calls



    DBManager_remove_stale_files->>execute: calls



    DBManager_remove_stale_files->>delete: calls



    DBManager_remove_stale_files->>where: calls



    DBManager_remove_stale_files->>in_: calls



    DBManager_remove_stale_files->>commit: calls



    DBManager_remove_stale_files->>rollback: calls


```

## Flow from `DBQueryAPI.find_callers_of`

The `find_callers_of` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `execute`, and `SessionLocal`.

```mermaid
sequenceDiagram
    participant Start as DBQueryAPI_find_callers_of


    DBQueryAPI_find_callers_of->>SessionLocal: calls



    DBQueryAPI_find_callers_of->>select: calls



    DBQueryAPI_find_callers_of->>join: calls



    DBQueryAPI_find_callers_of->>where: calls



    DBQueryAPI_find_callers_of->>where: calls



    DBQueryAPI_find_callers_of->>execute: calls



    DBQueryAPI_find_callers_of->>all: calls


```

## Flow from `DBQueryAPI.get_class_hierarchy`

The `get_class_hierarchy` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `execute`, and `SessionLocal`.

```mermaid
sequenceDiagram
    participant Start as DBQueryAPI_get_class_hierarchy


    DBQueryAPI_get_class_hierarchy->>SessionLocal: calls



    DBQueryAPI_get_class_hierarchy->>select: calls



    DBQueryAPI_get_class_hierarchy->>join: calls



    DBQueryAPI_get_class_hierarchy->>where: calls



    DBQueryAPI_get_class_hierarchy->>execute: calls



    DBQueryAPI_get_class_hierarchy->>all: calls


```

## Flow from `DBQueryAPI.get_module_structure`

The `get_module_structure` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 13 different components. The primary interactions involve `split`, `set`, and `query`.

```mermaid
sequenceDiagram
    participant Start as DBQueryAPI_get_module_structure


    DBQueryAPI_get_module_structure->>SessionLocal: calls



    DBQueryAPI_get_module_structure->>query: calls



    DBQueryAPI_get_module_structure->>all: calls



    DBQueryAPI_get_module_structure->>defaultdict: calls



    DBQueryAPI_get_module_structure->>set: calls



    DBQueryAPI_get_module_structure->>lstrip: calls



    DBQueryAPI_get_module_structure->>split: calls



    DBQueryAPI_get_module_structure->>len: calls



    DBQueryAPI_get_module_structure->>join: calls



    DBQueryAPI_get_module_structure->>append: calls



    DBQueryAPI_get_module_structure->>len: calls



    DBQueryAPI_get_module_structure->>len: calls



    DBQueryAPI_get_module_structure->>add: calls



    DBQueryAPI_get_module_structure->>items: calls



    DBQueryAPI_get_module_structure->>append: calls



    DBQueryAPI_get_module_structure->>list: calls


```

## Flow from `J.addOption`

The `addOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `hasOwnProperty`, `isArray`, and `addOptions`.

```mermaid
sequenceDiagram
    participant Start as J_addOption


    J_addOption->>isArray: calls



    J_addOption->>addOptions: calls



    J_addOption->>q: calls



    J_addOption->>hasOwnProperty: calls



    J_addOption->>trigger: calls


```

## Flow from `J.enable`

The `enable` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `unlock`.

```mermaid
sequenceDiagram
    participant Start as J_enable


    J_enable->>unlock: calls


```

## Flow from `J.hook`

The `hook` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `apply`.

```mermaid
sequenceDiagram
    participant Start as J_hook


    J_hook->>apply: calls



    J_hook->>apply: calls



    J_hook->>apply: calls


```

## Flow from `J.insertAtCaret`

The `insertAtCaret` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `setCaret` and `insertBefore`.

```mermaid
sequenceDiagram
    participant Start as J_insertAtCaret


    J_insertAtCaret->>insertBefore: calls



    J_insertAtCaret->>setCaret: calls


```

## Flow from `J.onBlur`

The `onBlur` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 35 different components. The primary interactions involve `setImages`, `setOptions`, and `createItem`.

```mermaid
sequenceDiagram
    participant Start as J_onBlur


    J_onBlur->>hasFocus: calls



    J_onBlur->>close: calls



    J_onBlur->>setActiveItem: calls



    J_onBlur->>setCaret: calls



    J_onBlur->>trigger: calls



    J_onBlur->>createItem: calls



    J_onBlur->>i: calls



    i->>off: calls



    i->>apply: calls



    i->>d: calls



    i->>call: calls



    i->>resolve: calls



    i->>then: calls



    i->>i: calls



    i->>i: calls



    i->>resolve: calls



    i->>then: calls



    i->>s: calls



    i->>i: calls



    i->>a: calls


```

## Flow from `J.render`

The `render` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `_render`.

```mermaid
sequenceDiagram
    participant Start as J_render


    J_render->>_render: calls


```

## Flow from `TestCppInheritance.test_inheritance_caller_is_child_class`

The `test_inheritance_caller_is_child_class` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 3 different components. The primary interactions involve `_parse`, `any`, and `dedent`.

```mermaid
sequenceDiagram
    participant Start as TestCppInheritance_test_inheritance_caller_is_child_class


    TestCppInheritance_test_inheritance_caller_is_child_class->>dedent: calls



    TestCppInheritance_test_inheritance_caller_is_child_class->>_parse: calls



    TestCppInheritance_test_inheritance_caller_is_child_class->>any: calls


```

## Flow from `selectNode`

The `selectNode` workflow represents a critical path in the system. When this flow is triggered, execution begins in `utils.js`. From there, it coordinates with 9 different components. The primary interactions involve `concat`, `selectNodes`, and `neighbourhoodHighlight`.

```mermaid
sequenceDiagram
    participant Start as selectNode


    selectNode->>selectNodes: calls



    selectNode->>neighbourhoodHighlight: calls



    neighbourhoodHighlight->>get: calls



    neighbourhoodHighlight->>getConnectedNodes: calls



    neighbourhoodHighlight->>concat: calls



    neighbourhoodHighlight->>getConnectedNodes: calls



    neighbourhoodHighlight->>hasOwnProperty: calls



    neighbourhoodHighlight->>push: calls



    neighbourhoodHighlight->>update: calls



    neighbourhoodHighlight->>hasOwnProperty: calls



    neighbourhoodHighlight->>push: calls



    neighbourhoodHighlight->>update: calls



    selectNodes->>selectNodes: calls



    selectNodes->>filterHighlight: calls



    filterHighlight->>get: calls



    filterHighlight->>hasOwnProperty: calls



    filterHighlight->>push: calls



    filterHighlight->>update: calls



    filterHighlight->>hasOwnProperty: calls



    filterHighlight->>push: calls


```

## Flow from `test_go_basic_symbols`

The `test_go_basic_symbols` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_go.py`. From there, it coordinates with 5 different components. The primary interactions involve `set_language`, `ASTParser`, and `dedent`.

```mermaid
sequenceDiagram
    participant Start as test_go_basic_symbols


    test_go_basic_symbols->>ASTParser: calls



    test_go_basic_symbols->>set_language: calls



    test_go_basic_symbols->>dedent: calls



    test_go_basic_symbols->>extract_symbols: calls



    test_go_basic_symbols->>len: calls


```

## Flow from `test_go_garbage_safety`

The `test_go_garbage_safety` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_go.py`. From there, it coordinates with 4 different components. The primary interactions involve `extract_dependencies`, `set_language`, and `ASTParser`.

```mermaid
sequenceDiagram
    participant Start as test_go_garbage_safety


    test_go_garbage_safety->>ASTParser: calls



    test_go_garbage_safety->>set_language: calls



    test_go_garbage_safety->>extract_dependencies: calls



    test_go_garbage_safety->>isinstance: calls


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

The `test_python_garbage_safety` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_ast_parser.py`. From there, it coordinates with 6 different components. The primary interactions involve `extract_dependencies`, `set_language`, and `ASTParser`.

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


---
*Generated by DECODE NLG | [← Back to Index](index.md)*