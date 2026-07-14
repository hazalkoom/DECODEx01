# Data Flow
> **Onboarding question:** How does information move?


## Workflow: main

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `Network`, `first`, and `in_`.

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

The `test_cpp_function_calls_remain_call_kind` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 2 different components. The primary interactions involve `len` and `_parse`.

```mermaid
graph TD
    Start[TestCppInheritance_test_cpp_function_calls_remain_call_kind]


    TestCppInheritance_test_cpp_function_calls_remain_call_kind --> _parse



    TestCppInheritance_test_cpp_function_calls_remain_call_kind --> len


```

## Workflow: DBQueryAPI.get_domain_entities

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `any`, `SessionLocal`, and `join`.

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

The `onClick` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `clearActiveItems`, `focus`, and `blur`.

```mermaid
graph TD
    Start[J_onClick]


    J_onClick --> clearActiveItems



    J_onClick --> focus



    J_onClick --> blur



    J_onClick --> focus


```

## Workflow: J.setup

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 57 different components. The primary interactions involve `preload`, `onFocus`, and `stopPropagation`.

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

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `registerOptionGroup`, `y`, and `addOptions`.

```mermaid
graph TD
    Start[J_setupOptions]


    J_setupOptions --> addOptions



    J_setupOptions --> y



    J_setupOptions --> registerOptionGroup


```

## Workflow: J.setupTemplates

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 73 different components. The primary interactions involve `random`, `vg`, and `split`.

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

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `len`, `select`, and `SessionLocal`.

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

The `ingest_project_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 7 different components. The primary interactions involve `len`, `SessionLocal`, and `execute`.

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

## Workflow: DBQueryAPI.find_files_importing

The `find_files_importing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 7 different components. The primary interactions involve `select`, `where`, and `SessionLocal`.

```mermaid
graph TD
    Start[DBQueryAPI_find_files_importing]


    DBQueryAPI_find_files_importing --> SessionLocal



    DBQueryAPI_find_files_importing --> select



    DBQueryAPI_find_files_importing --> join



    DBQueryAPI_find_files_importing --> where



    DBQueryAPI_find_files_importing --> like



    DBQueryAPI_find_files_importing --> execute



    DBQueryAPI_find_files_importing --> all


```

## Workflow: DBQueryAPI.get_class_hierarchy

The `get_class_hierarchy` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `where`, and `SessionLocal`.

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

## Workflow: J.addOptionGroup

The `addOptionGroup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `registerOptionGroup` and `trigger`.

```mermaid
graph TD
    Start[J_addOptionGroup]


    J_addOptionGroup --> registerOptionGroup



    J_addOptionGroup --> trigger


```

## Workflow: J.clearActiveItems

The `clearActiveItems` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `S`.

```mermaid
graph TD
    Start[J_clearActiveItems]


    J_clearActiveItems --> S


```

## Workflow: J.clearOptions

The `clearOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `clearCache`, `y`, and `trigger`.

```mermaid
graph TD
    Start[J_clearOptions]


    J_clearOptions --> clearCache



    J_clearOptions --> y



    J_clearOptions --> indexOf



    J_clearOptions --> trigger


```

## Workflow: J.destroy

The `destroy` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `trigger`, `_destroy`, and `off`.

```mermaid
graph TD
    Start[J_destroy]


    J_destroy --> trigger



    J_destroy --> off



    J_destroy --> remove



    J_destroy --> remove



    J_destroy --> S



    J_destroy --> _destroy


```

## Workflow: J.onInput

The `onInput` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `trigger`, `load`, and `refreshOptions`.

```mermaid
graph TD
    Start[J_onInput]


    J_onInput --> inputValue



    J_onInput --> call



    J_onInput --> load



    J_onInput --> refreshOptions



    J_onInput --> trigger


```

## Workflow: J.selectable

The `selectable` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `querySelectorAll`.

```mermaid
graph TD
    Start[J_selectable]


    J_selectable --> querySelectorAll


```

## Workflow: J.setActiveItemClass

The `setActiveItemClass` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 6 different components. The primary interactions involve `trigger`, `push`, and `querySelector`.

```mermaid
graph TD
    Start[J_setActiveItemClass]


    J_setActiveItemClass --> querySelector



    J_setActiveItemClass --> S



    J_setActiveItemClass --> C



    J_setActiveItemClass --> trigger



    J_setActiveItemClass --> indexOf



    J_setActiveItemClass --> push



    C --> push


```

## Workflow: J.uncacheValue

The `uncacheValue` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `remove` and `getOption`.

```mermaid
graph TD
    Start[J_uncacheValue]


    J_uncacheValue --> getOption



    J_uncacheValue --> remove


```

## Workflow: TestCppReturnTypes.test_bool_return_type

The `test_bool_return_type` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_return_types.py`. From there, it coordinates with 1 different components. The primary interactions involve `_parse`.

```mermaid
graph TD
    Start[TestCppReturnTypes_test_bool_return_type]


    TestCppReturnTypes_test_bool_return_type --> _parse


```

## Workflow: qg

The `qg` workflow represents a critical path in the system. When this flow is triggered, execution begins in `vis-network.min.js`. From there, it coordinates with 10 different components. The primary interactions involve `mg`, `jg`, and `push`.

```mermaid
graph TD
    Start[qg]


    qg --> jg



    qg --> jg



    qg --> filter



    qg --> mg



    qg --> push



    qg --> Rg



    qg --> concat



    jg --> call



    Rg --> Ig



    Rg --> push



    Rg --> sort



    Rg --> sort



    Ig --> indexOf


```

## Workflow: test_bash_basic_symbols

The `test_bash_basic_symbols` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_bash.py`. From there, it coordinates with 5 different components. The primary interactions involve `len`, `ASTParser`, and `dedent`.

```mermaid
graph TD
    Start[test_bash_basic_symbols]


    test_bash_basic_symbols --> ASTParser



    test_bash_basic_symbols --> set_language



    test_bash_basic_symbols --> dedent



    test_bash_basic_symbols --> extract_symbols



    test_bash_basic_symbols --> len


```

## Workflow: test_get_class_hierarchy_success

The `test_get_class_hierarchy_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 2 different components. The primary interactions involve `len` and `get_class_hierarchy`.

```mermaid
graph TD
    Start[test_get_class_hierarchy_success]


    test_get_class_hierarchy_success --> get_class_hierarchy



    test_get_class_hierarchy_success --> len


```

## Workflow: test_get_file_outline_success

The `test_get_file_outline_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api.py`. From there, it coordinates with 3 different components. The primary interactions involve `len`, `get_file_outline`, and `sorted`.

```mermaid
graph TD
    Start[test_get_file_outline_success]


    test_get_file_outline_success --> get_file_outline



    test_get_file_outline_success --> len



    test_get_file_outline_success --> sorted


```

## Workflow: test_js_es6_exports

The `test_js_es6_exports` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_javascript.py`. From there, it coordinates with 5 different components. The primary interactions involve `len`, `ASTParser`, and `extract_dependencies`.

```mermaid
graph TD
    Start[test_js_es6_exports]


    test_js_es6_exports --> ASTParser



    test_js_es6_exports --> set_language



    test_js_es6_exports --> dedent



    test_js_es6_exports --> extract_dependencies



    test_js_es6_exports --> len


```

## Workflow: test_remove_stale_files_cascade

The `test_remove_stale_files_cascade` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 7 different components. The primary interactions involve `len`, `SessionLocal`, and `first`.

```mermaid
graph TD
    Start[test_remove_stale_files_cascade]


    test_remove_stale_files_cascade --> SessionLocal



    test_remove_stale_files_cascade --> query



    test_remove_stale_files_cascade --> count



    test_remove_stale_files_cascade --> query



    test_remove_stale_files_cascade --> count



    test_remove_stale_files_cascade --> query



    test_remove_stale_files_cascade --> count



    test_remove_stale_files_cascade --> remove_stale_files



    test_remove_stale_files_cascade --> SessionLocal



    test_remove_stale_files_cascade --> query



    test_remove_stale_files_cascade --> count



    test_remove_stale_files_cascade --> query



    test_remove_stale_files_cascade --> first



    test_remove_stale_files_cascade --> query



    test_remove_stale_files_cascade --> all


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*