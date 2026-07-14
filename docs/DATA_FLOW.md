# Data Flow
> **Onboarding question:** How does information move?


## Workflow: main

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `connect`, `FileSystemLoader`, and `execute`.

```mermaid
graph TD
    Start[main]


    main --> ArgumentParser



    main --> add_subparsers



    main --> add_parser



    main --> add_argument



    main --> add_parser



    main --> add_argument



    main --> add_parser



    main --> add_argument



    main --> add_argument



    main --> add_argument



    main --> add_parser



    main --> add_argument



    main --> add_argument



    main --> add_parser



    main --> add_argument


```

## Workflow: TestCppInheritance.test_cpp_function_calls_remain_call_kind

The `test_cpp_function_calls_remain_call_kind` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 2 different components. The primary interactions involve `_parse` and `len`.

```mermaid
graph TD
    Start[TestCppInheritance_test_cpp_function_calls_remain_call_kind]


    TestCppInheritance_test_cpp_function_calls_remain_call_kind --> _parse



    TestCppInheritance_test_cpp_function_calls_remain_call_kind --> len


```

## Workflow: DBQueryAPI.get_domain_entities

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `filter`, `query`, and `count`.

```mermaid
graph TD
    Start[DBQueryAPI_get_domain_entities]


    DBQueryAPI_get_domain_entities --> SessionLocal



    DBQueryAPI_get_domain_entities --> query



    DBQueryAPI_get_domain_entities --> join



    DBQueryAPI_get_domain_entities --> filter



    DBQueryAPI_get_domain_entities --> all



    DBQueryAPI_get_domain_entities --> defaultdict



    DBQueryAPI_get_domain_entities --> query



    DBQueryAPI_get_domain_entities --> all



    DBQueryAPI_get_domain_entities --> any



    DBQueryAPI_get_domain_entities --> query



    DBQueryAPI_get_domain_entities --> filter



    DBQueryAPI_get_domain_entities --> in_



    DBQueryAPI_get_domain_entities --> count



    DBQueryAPI_get_domain_entities --> append



    DBQueryAPI_get_domain_entities --> sort


```

## Workflow: J.onClick

The `onClick` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `clearActiveItems`, `blur`, and `focus`.

```mermaid
graph TD
    Start[J_onClick]


    J_onClick --> clearActiveItems



    J_onClick --> focus



    J_onClick --> blur



    J_onClick --> focus


```

## Workflow: J.setup

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 57 different components. The primary interactions involve `close`, `M`, and `h`.

```mermaid
graph TD
    Start[J_setup]


    J_setup --> P



    J_setup --> P



    J_setup --> M



    J_setup --> replace



    J_setup --> querySelector



    J_setup --> bind



    J_setup --> B



    J_setup --> P



    J_setup --> M



    J_setup --> P



    J_setup --> P



    J_setup --> join



    J_setup --> C



    J_setup --> P



    J_setup --> P


```

## Workflow: J.setupOptions

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `registerOptionGroup`, `addOptions`, and `y`.

```mermaid
graph TD
    Start[J_setupOptions]


    J_setupOptions --> addOptions



    J_setupOptions --> y



    J_setupOptions --> registerOptionGroup


```

## Workflow: J.setupTemplates

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 73 different components. The primary interactions involve `setImages`, `pg`, and `setOptions`.

```mermaid
graph TD
    Start[J_setupTemplates]


    J_setupTemplates --> createElement



    J_setupTemplates --> appendChild



    J_setupTemplates --> t



    J_setupTemplates --> i



    J_setupTemplates --> i



    J_setupTemplates --> t



    J_setupTemplates --> assign



    i --> off



    i --> apply



    i --> d



    i --> call



    i --> resolve



    i --> then



    i --> i



    i --> i


```

## Workflow: J.setupCallbacks

The `setupCallbacks` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `on`.

```mermaid
graph TD
    Start[J_setupCallbacks]


    J_setupCallbacks --> on


```

## Workflow: test_schema_setup

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `execute`, `select`, and `SessionLocal`.

```mermaid
graph TD
    Start[test_schema_setup]


    test_schema_setup --> SessionLocal



    test_schema_setup --> execute



    test_schema_setup --> select



    test_schema_setup --> all



    test_schema_setup --> execute



    test_schema_setup --> select



    test_schema_setup --> all



    test_schema_setup --> execute



    test_schema_setup --> select



    test_schema_setup --> all



    test_schema_setup --> execute



    test_schema_setup --> select



    test_schema_setup --> all



    test_schema_setup --> len



    test_schema_setup --> len


```

## Workflow: J.registerOption

The `registerOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `addOption`.

```mermaid
graph TD
    Start[J_registerOption]


    J_registerOption --> addOption


```

## Workflow: J.registerOptionGroup

The `registerOptionGroup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `q`.

```mermaid
graph TD
    Start[J_registerOptionGroup]


    J_registerOptionGroup --> q


```

## Workflow: ArchitectureGenerator.gather_data

The `gather_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `architecture.py`. From there, it coordinates with 2 different components. The primary interactions involve `get_module_structure` and `get_cross_module_edges`.

```mermaid
graph TD
    Start[ArchitectureGenerator_gather_data]


    ArchitectureGenerator_gather_data --> get_module_structure



    ArchitectureGenerator_gather_data --> get_cross_module_edges


```

## Workflow: DBManager.remove_stale_files

The `remove_stale_files` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 9 different components. The primary interactions involve `range`, `in_`, and `rollback`.

```mermaid
graph TD
    Start[DBManager_remove_stale_files]


    DBManager_remove_stale_files --> SessionLocal



    DBManager_remove_stale_files --> range



    DBManager_remove_stale_files --> len



    DBManager_remove_stale_files --> execute



    DBManager_remove_stale_files --> delete



    DBManager_remove_stale_files --> where



    DBManager_remove_stale_files --> in_



    DBManager_remove_stale_files --> commit



    DBManager_remove_stale_files --> rollback


```

## Workflow: DBQueryAPI.find_callers_of

The `find_callers_of` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `execute`, and `SessionLocal`.

```mermaid
graph TD
    Start[DBQueryAPI_find_callers_of]


    DBQueryAPI_find_callers_of --> SessionLocal



    DBQueryAPI_find_callers_of --> select



    DBQueryAPI_find_callers_of --> join



    DBQueryAPI_find_callers_of --> where



    DBQueryAPI_find_callers_of --> where



    DBQueryAPI_find_callers_of --> execute



    DBQueryAPI_find_callers_of --> all


```

## Workflow: DBQueryAPI.get_class_hierarchy

The `get_class_hierarchy` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `execute`, and `SessionLocal`.

```mermaid
graph TD
    Start[DBQueryAPI_get_class_hierarchy]


    DBQueryAPI_get_class_hierarchy --> SessionLocal



    DBQueryAPI_get_class_hierarchy --> select



    DBQueryAPI_get_class_hierarchy --> join



    DBQueryAPI_get_class_hierarchy --> where



    DBQueryAPI_get_class_hierarchy --> execute



    DBQueryAPI_get_class_hierarchy --> all


```

## Workflow: DBQueryAPI.get_module_structure

The `get_module_structure` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 13 different components. The primary interactions involve `split`, `set`, and `query`.

```mermaid
graph TD
    Start[DBQueryAPI_get_module_structure]


    DBQueryAPI_get_module_structure --> SessionLocal



    DBQueryAPI_get_module_structure --> query



    DBQueryAPI_get_module_structure --> all



    DBQueryAPI_get_module_structure --> defaultdict



    DBQueryAPI_get_module_structure --> set



    DBQueryAPI_get_module_structure --> lstrip



    DBQueryAPI_get_module_structure --> split



    DBQueryAPI_get_module_structure --> len



    DBQueryAPI_get_module_structure --> join



    DBQueryAPI_get_module_structure --> append



    DBQueryAPI_get_module_structure --> len



    DBQueryAPI_get_module_structure --> len



    DBQueryAPI_get_module_structure --> add



    DBQueryAPI_get_module_structure --> items



    DBQueryAPI_get_module_structure --> append


```

## Workflow: J.addOption

The `addOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `hasOwnProperty`, `isArray`, and `addOptions`.

```mermaid
graph TD
    Start[J_addOption]


    J_addOption --> isArray



    J_addOption --> addOptions



    J_addOption --> q



    J_addOption --> hasOwnProperty



    J_addOption --> trigger


```

## Workflow: J.enable

The `enable` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `unlock`.

```mermaid
graph TD
    Start[J_enable]


    J_enable --> unlock


```

## Workflow: J.hook

The `hook` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `apply`.

```mermaid
graph TD
    Start[J_hook]


    J_hook --> apply



    J_hook --> apply



    J_hook --> apply


```

## Workflow: J.insertAtCaret

The `insertAtCaret` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `setCaret` and `insertBefore`.

```mermaid
graph TD
    Start[J_insertAtCaret]


    J_insertAtCaret --> insertBefore



    J_insertAtCaret --> setCaret


```

## Workflow: J.onBlur

The `onBlur` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 32 different components. The primary interactions involve `setImages`, `setOptions`, and `createItem`.

```mermaid
graph TD
    Start[J_onBlur]


    J_onBlur --> hasFocus



    J_onBlur --> close



    J_onBlur --> setActiveItem



    J_onBlur --> setCaret



    J_onBlur --> trigger



    J_onBlur --> createItem



    J_onBlur --> i



    i --> off



    i --> apply



    i --> d



    i --> call



    i --> resolve



    i --> then



    i --> i



    i --> i


```

## Workflow: J.render

The `render` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `_render`.

```mermaid
graph TD
    Start[J_render]


    J_render --> _render


```

## Workflow: TestCppInheritance.test_inheritance_caller_is_child_class

The `test_inheritance_caller_is_child_class` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 3 different components. The primary interactions involve `_parse`, `any`, and `dedent`.

```mermaid
graph TD
    Start[TestCppInheritance_test_inheritance_caller_is_child_class]


    TestCppInheritance_test_inheritance_caller_is_child_class --> dedent



    TestCppInheritance_test_inheritance_caller_is_child_class --> _parse



    TestCppInheritance_test_inheritance_caller_is_child_class --> any


```

## Workflow: selectNode

The `selectNode` workflow represents a critical path in the system. When this flow is triggered, execution begins in `utils.js`. From there, it coordinates with 9 different components. The primary interactions involve `concat`, `selectNodes`, and `neighbourhoodHighlight`.

```mermaid
graph TD
    Start[selectNode]


    selectNode --> selectNodes



    selectNode --> neighbourhoodHighlight



    neighbourhoodHighlight --> get



    neighbourhoodHighlight --> getConnectedNodes



    neighbourhoodHighlight --> concat



    neighbourhoodHighlight --> getConnectedNodes



    neighbourhoodHighlight --> hasOwnProperty



    neighbourhoodHighlight --> push



    neighbourhoodHighlight --> update



    neighbourhoodHighlight --> hasOwnProperty



    neighbourhoodHighlight --> push



    neighbourhoodHighlight --> update



    selectNodes --> selectNodes



    selectNodes --> filterHighlight



    filterHighlight --> get


```

## Workflow: test_go_basic_symbols

The `test_go_basic_symbols` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_go.py`. From there, it coordinates with 5 different components. The primary interactions involve `set_language`, `ASTParser`, and `dedent`.

```mermaid
graph TD
    Start[test_go_basic_symbols]


    test_go_basic_symbols --> ASTParser



    test_go_basic_symbols --> set_language



    test_go_basic_symbols --> dedent



    test_go_basic_symbols --> extract_symbols



    test_go_basic_symbols --> len


```

## Workflow: test_go_garbage_safety

The `test_go_garbage_safety` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_go.py`. From there, it coordinates with 4 different components. The primary interactions involve `extract_dependencies`, `set_language`, and `ASTParser`.

```mermaid
graph TD
    Start[test_go_garbage_safety]


    test_go_garbage_safety --> ASTParser



    test_go_garbage_safety --> set_language



    test_go_garbage_safety --> extract_dependencies



    test_go_garbage_safety --> isinstance


```

## Workflow: test_language_detection

The `test_language_detection` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_language_detector.py`. From there, it coordinates with 1 different components. The primary interactions involve `detect_language`.

```mermaid
graph TD
    Start[test_language_detection]


    test_language_detection --> detect_language



    test_language_detection --> detect_language



    test_language_detection --> detect_language



    test_language_detection --> detect_language



    test_language_detection --> detect_language



    test_language_detection --> detect_language


```

## Workflow: test_python_garbage_safety

The `test_python_garbage_safety` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_ast_parser.py`. From there, it coordinates with 6 different components. The primary interactions involve `extract_dependencies`, `set_language`, and `ASTParser`.

```mermaid
graph TD
    Start[test_python_garbage_safety]


    test_python_garbage_safety --> ASTParser



    test_python_garbage_safety --> set_language



    test_python_garbage_safety --> dedent



    test_python_garbage_safety --> extract_symbols



    test_python_garbage_safety --> extract_dependencies



    test_python_garbage_safety --> isinstance



    test_python_garbage_safety --> isinstance


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*