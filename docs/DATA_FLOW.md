# Data Flow
> **Onboarding question:** How does information move?


## Workflow: main

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `add`, `open`, and `Network`.

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

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `any`, `all`, and `query`.

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

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 57 different components. The primary interactions involve `o`, `insertAdjacentElement`, and `create`.

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

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 73 different components. The primary interactions involve `Cm`, `_determineBrowserMethod`, and `lu`.

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

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `select`, `execute`, and `all`.

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

## Workflow: DBQueryAPI.get_class_hierarchy_full

The `get_class_hierarchy_full` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `execute`, and `all`.

```mermaid
graph TD
    Start[DBQueryAPI_get_class_hierarchy_full]


    DBQueryAPI_get_class_hierarchy_full --> SessionLocal



    DBQueryAPI_get_class_hierarchy_full --> select



    DBQueryAPI_get_class_hierarchy_full --> join



    DBQueryAPI_get_class_hierarchy_full --> where



    DBQueryAPI_get_class_hierarchy_full --> execute



    DBQueryAPI_get_class_hierarchy_full --> all


```

## Workflow: DBQueryAPI.get_dependency_clusters

The `get_dependency_clusters` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 1 different components. The primary interactions involve `get_module_structure`.

```mermaid
graph TD
    Start[DBQueryAPI_get_dependency_clusters]


    DBQueryAPI_get_dependency_clusters --> get_module_structure


```

## Workflow: J.addOption

The `addOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `q`, `addOptions`, and `hasOwnProperty`.

```mermaid
graph TD
    Start[J_addOption]


    J_addOption --> isArray



    J_addOption --> addOptions



    J_addOption --> q



    J_addOption --> hasOwnProperty



    J_addOption --> trigger


```

## Workflow: J.onFocus

The `onFocus` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 7 different components. The primary interactions involve `refreshOptions`, `H`, and `showInput`.

```mermaid
graph TD
    Start[J_onFocus]


    J_onFocus --> blur



    J_onFocus --> H



    J_onFocus --> preload



    J_onFocus --> trigger



    J_onFocus --> showInput



    J_onFocus --> refreshOptions



    J_onFocus --> refreshState


```

## Workflow: J.selectAll

The `selectAll` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `hideInput`, `controlChildren`, and `close`.

```mermaid
graph TD
    Start[J_selectAll]


    J_selectAll --> controlChildren



    J_selectAll --> hideInput



    J_selectAll --> close



    J_selectAll --> C



    C --> push


```

## Workflow: ModuleGuideGenerator.gather_data

The `gather_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `module_guide.py`. From there, it coordinates with 1 different components. The primary interactions involve `get_module_structure`.

```mermaid
graph TD
    Start[ModuleGuideGenerator_gather_data]


    ModuleGuideGenerator_gather_data --> get_module_structure


```

## Workflow: ProjectMapGenerator.gather_data

The `gather_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `project_map.py`. From there, it coordinates with 1 different components. The primary interactions involve `get_module_structure`.

```mermaid
graph TD
    Start[ProjectMapGenerator_gather_data]


    ProjectMapGenerator_gather_data --> get_module_structure


```

## Workflow: TestCppInheritance.test_inheritance_caller_is_child_class

The `test_inheritance_caller_is_child_class` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 3 different components. The primary interactions involve `dedent`, `any`, and `_parse`.

```mermaid
graph TD
    Start[TestCppInheritance_test_inheritance_caller_is_child_class]


    TestCppInheritance_test_inheritance_caller_is_child_class --> dedent



    TestCppInheritance_test_inheritance_caller_is_child_class --> _parse



    TestCppInheritance_test_inheritance_caller_is_child_class --> any


```

## Workflow: b.getScoreFunction

The `getScoreFunction` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `prepareSearch` and `_getScoreFunction`.

```mermaid
graph TD
    Start[b_getScoreFunction]


    b_getScoreFunction --> prepareSearch



    b_getScoreFunction --> _getScoreFunction


```

## Workflow: highlightFilter

The `highlightFilter` workflow represents a critical path in the system. When this flow is triggered, execution begins in `utils.js`. From there, it coordinates with 8 different components. The primary interactions involve `toString`, `update`, and `selectNodes`.

```mermaid
graph TD
    Start[highlightFilter]


    highlightFilter --> get



    highlightFilter --> includes



    highlightFilter --> toString



    highlightFilter --> push



    highlightFilter --> get



    highlightFilter --> includes



    highlightFilter --> toString



    highlightFilter --> push



    highlightFilter --> push



    highlightFilter --> selectNodes



    selectNodes --> selectNodes



    selectNodes --> filterHighlight



    filterHighlight --> get



    filterHighlight --> hasOwnProperty



    filterHighlight --> push


```

## Workflow: set_sqlite_pragma

The `set_sqlite_pragma` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 3 different components. The primary interactions involve `close`, `cursor`, and `execute`.

```mermaid
graph TD
    Start[set_sqlite_pragma]


    set_sqlite_pragma --> cursor



    set_sqlite_pragma --> execute



    set_sqlite_pragma --> execute



    set_sqlite_pragma --> execute



    set_sqlite_pragma --> execute



    set_sqlite_pragma --> close


```

## Workflow: test_cpp_inline_functions

The `test_cpp_inline_functions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_cpp.py`. From there, it coordinates with 4 different components. The primary interactions involve `extract_symbols`, `len`, and `set_language`.

```mermaid
graph TD
    Start[test_cpp_inline_functions]


    test_cpp_inline_functions --> ASTParser



    test_cpp_inline_functions --> set_language



    test_cpp_inline_functions --> extract_symbols



    test_cpp_inline_functions --> len


```

## Workflow: test_find_callers_of_missing

The `test_find_callers_of_missing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 3 different components. The primary interactions involve `find_callers_of`, `len`, and `isinstance`.

```mermaid
graph TD
    Start[test_find_callers_of_missing]


    test_find_callers_of_missing --> find_callers_of



    test_find_callers_of_missing --> isinstance



    test_find_callers_of_missing --> len


```

## Workflow: test_find_calls_by_missing

The `test_find_calls_by_missing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 3 different components. The primary interactions involve `find_calls_by`, `len`, and `isinstance`.

```mermaid
graph TD
    Start[test_find_calls_by_missing]


    test_find_calls_by_missing --> find_calls_by



    test_find_calls_by_missing --> isinstance



    test_find_calls_by_missing --> len


```

## Workflow: test_js_basic_symbols

The `test_js_basic_symbols` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_javascript.py`. From there, it coordinates with 5 different components. The primary interactions involve `dedent`, `ASTParser`, and `len`.

```mermaid
graph TD
    Start[test_js_basic_symbols]


    test_js_basic_symbols --> ASTParser



    test_js_basic_symbols --> set_language



    test_js_basic_symbols --> dedent



    test_js_basic_symbols --> extract_symbols



    test_js_basic_symbols --> len


```

## Workflow: test_qa_sloppy_shebangs

The `test_qa_sloppy_shebangs` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_language_qa.py`. From there, it coordinates with 1 different components. The primary interactions involve `detect_language`.

```mermaid
graph TD
    Start[test_qa_sloppy_shebangs]


    test_qa_sloppy_shebangs --> detect_language


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*