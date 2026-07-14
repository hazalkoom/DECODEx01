# Data Flow
> **Onboarding question:** How does information move?


## Workflow: main

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `Session`, `write`, and `Network`.

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

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `defaultdict`, `any`, and `filter`.

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

The `onClick` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `blur`, `focus`, and `clearActiveItems`.

```mermaid
graph TD
    Start[J_onClick]


    J_onClick --> clearActiveItems



    J_onClick --> focus



    J_onClick --> blur



    J_onClick --> focus


```

## Workflow: J.setup

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 57 different components. The primary interactions involve `enable`, `removeEventListener`, and `v`.

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

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `y`, `registerOptionGroup`, and `addOptions`.

```mermaid
graph TD
    Start[J_setupOptions]


    J_setupOptions --> addOptions



    J_setupOptions --> y



    J_setupOptions --> registerOptionGroup


```

## Workflow: J.setupTemplates

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 73 different components. The primary interactions involve `a`, `$d`, and `zn`.

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



    t --> set



    t --> vg



    t --> handler



    t --> init



    t --> Rv



    t --> qv



    t --> py



    t --> pg


```

## Workflow: J.setupCallbacks

The `setupCallbacks` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `on`.

```mermaid
graph TD
    Start[J_setupCallbacks]


    J_setupCallbacks --> on


```

## Workflow: test_schema_setup

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `SessionLocal`, `execute`, and `len`.

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

## Workflow: DBManager.ingest_project_data

The `ingest_project_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 7 different components. The primary interactions involve `commit`, `SessionLocal`, and `execute`.

```mermaid
graph TD
    Start[DBManager_ingest_project_data]


    DBManager_ingest_project_data --> SessionLocal



    DBManager_ingest_project_data --> execute



    DBManager_ingest_project_data --> insert



    DBManager_ingest_project_data --> range



    DBManager_ingest_project_data --> len



    DBManager_ingest_project_data --> execute



    DBManager_ingest_project_data --> insert



    DBManager_ingest_project_data --> range



    DBManager_ingest_project_data --> len



    DBManager_ingest_project_data --> execute



    DBManager_ingest_project_data --> insert



    DBManager_ingest_project_data --> range



    DBManager_ingest_project_data --> len



    DBManager_ingest_project_data --> execute



    DBManager_ingest_project_data --> insert


```

## Workflow: DocsCoordinator.generate_all

The `generate_all` workflow represents a critical path in the system. When this flow is triggered, execution begins in `coordinator.py`. From there, it coordinates with 3 different components. The primary interactions involve `makedirs`, `_render_index`, and `generate`.

```mermaid
graph TD
    Start[DocsCoordinator_generate_all]


    DocsCoordinator_generate_all --> makedirs



    DocsCoordinator_generate_all --> generate



    DocsCoordinator_generate_all --> _render_index


```

## Workflow: J.canCreate

The `canCreate` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `call`.

```mermaid
graph TD
    Start[J_canCreate]


    J_canCreate --> call


```

## Workflow: J.clearActiveItems

The `clearActiveItems` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `S`.

```mermaid
graph TD
    Start[J_clearActiveItems]


    J_clearActiveItems --> S


```

## Workflow: J.controlChildren

The `controlChildren` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `from` and `querySelectorAll`.

```mermaid
graph TD
    Start[J_controlChildren]


    J_controlChildren --> from



    J_controlChildren --> querySelectorAll


```

## Workflow: J.inputState

The `inputState` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `setTextboxValue`, `toggle`, and `contains`.

```mermaid
graph TD
    Start[J_inputState]


    J_inputState --> contains



    J_inputState --> P



    J_inputState --> setTextboxValue



    J_inputState --> P



    J_inputState --> toggle


```

## Workflow: J.o

The `o` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `w`, `N`, and `append`.

```mermaid
graph TD
    Start[J_o]


    J_o --> w



    J_o --> N



    J_o --> N



    J_o --> append



    J_o --> push


```

## Workflow: J.onPaste

The `onPaste` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 9 different components. The primary interactions involve `H`, `y`, and `inputValue`.

```mermaid
graph TD
    Start[J_onPaste]


    J_onPaste --> isFull



    J_onPaste --> H



    J_onPaste --> setTimeout



    J_onPaste --> inputValue



    J_onPaste --> match



    J_onPaste --> trim



    J_onPaste --> split



    J_onPaste --> y



    J_onPaste --> createItem


```

## Workflow: J.removeItem

The `removeItem` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 14 different components. The primary interactions involve `positionDropdown`, `hasOwnProperty`, and `L`.

```mermaid
graph TD
    Start[J_removeItem]


    J_removeItem --> getItem



    J_removeItem --> L



    J_removeItem --> remove



    J_removeItem --> contains



    J_removeItem --> indexOf



    J_removeItem --> splice



    J_removeItem --> S



    J_removeItem --> splice



    J_removeItem --> hasOwnProperty



    J_removeItem --> removeOption



    J_removeItem --> setCaret



    J_removeItem --> updateOriginalInput



    J_removeItem --> refreshState



    J_removeItem --> positionDropdown



    J_removeItem --> trigger


```

## Workflow: J.selectAll

The `selectAll` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `hideInput`, `close`, and `C`.

```mermaid
graph TD
    Start[J_selectAll]


    J_selectAll --> controlChildren



    J_selectAll --> hideInput



    J_selectAll --> close



    J_selectAll --> C



    C --> push


```

## Workflow: TestCppReturnTypes._parse

The `_parse` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_return_types.py`. From there, it coordinates with 3 different components. The primary interactions involve `analyze_file`, `ASTParser`, and `set_language`.

```mermaid
graph TD
    Start[TestCppReturnTypes__parse]


    TestCppReturnTypes__parse --> ASTParser



    TestCppReturnTypes__parse --> set_language



    TestCppReturnTypes__parse --> analyze_file


```

## Workflow: b.getSortFunction

The `getSortFunction` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `_getSortFunction` and `prepareSearch`.

```mermaid
graph TD
    Start[b_getSortFunction]


    b_getSortFunction --> prepareSearch



    b_getSortFunction --> _getSortFunction


```

## Workflow: test_cpp_nested_namespaces

The `test_cpp_nested_namespaces` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_cpp.py`. From there, it coordinates with 5 different components. The primary interactions involve `dedent`, `extract_symbols`, and `ASTParser`.

```mermaid
graph TD
    Start[test_cpp_nested_namespaces]


    test_cpp_nested_namespaces --> ASTParser



    test_cpp_nested_namespaces --> set_language



    test_cpp_nested_namespaces --> dedent



    test_cpp_nested_namespaces --> extract_symbols



    test_cpp_nested_namespaces --> len


```

## Workflow: test_find_calls_by_success

The `test_find_calls_by_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 2 different components. The primary interactions involve `find_calls_by` and `len`.

```mermaid
graph TD
    Start[test_find_calls_by_success]


    test_find_calls_by_success --> find_calls_by



    test_find_calls_by_success --> len


```

## Workflow: test_find_files_importing_success

The `test_find_files_importing_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api.py`. From there, it coordinates with 2 different components. The primary interactions involve `len` and `find_files_importing`.

```mermaid
graph TD
    Start[test_find_files_importing_success]


    test_find_files_importing_success --> find_files_importing



    test_find_files_importing_success --> len



    test_find_files_importing_success --> find_files_importing



    test_find_files_importing_success --> len


```

## Workflow: test_json_safely_ignored

The `test_json_safely_ignored` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_json.py`. From there, it coordinates with 4 different components. The primary interactions involve `extract_symbols`, `ASTParser`, and `set_language`.

```mermaid
graph TD
    Start[test_json_safely_ignored]


    test_json_safely_ignored --> ASTParser



    test_json_safely_ignored --> set_language



    test_json_safely_ignored --> extract_symbols



    test_json_safely_ignored --> extract_dependencies


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*