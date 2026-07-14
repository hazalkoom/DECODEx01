# Call Flow
> **Onboarding question:** What happens during execution?


## Flow from `main`

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `add`, `open`, and `Network`.

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

The `test_cpp_function_calls_remain_call_kind` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 2 different components. The primary interactions involve `len` and `_parse`.

```mermaid
sequenceDiagram
    participant Start as TestCppInheritance_test_cpp_function_calls_remain_call_kind


    TestCppInheritance_test_cpp_function_calls_remain_call_kind->>_parse: calls



    TestCppInheritance_test_cpp_function_calls_remain_call_kind->>len: calls


```

## Flow from `DBQueryAPI.get_domain_entities`

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `any`, `all`, and `query`.

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

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 58 different components. The primary interactions involve `o`, `insertAdjacentElement`, and `create`.

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

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `y`, `registerOptionGroup`, and `addOptions`.

```mermaid
sequenceDiagram
    participant Start as J_setupOptions


    J_setupOptions->>addOptions: calls



    J_setupOptions->>y: calls



    J_setupOptions->>registerOptionGroup: calls


```

## Flow from `J.setupTemplates`

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 77 different components. The primary interactions involve `add`, `off`, and `has`.

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

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `select`, `execute`, and `all`.

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

## Flow from `DBQueryAPI.get_class_hierarchy_full`

The `get_class_hierarchy_full` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `execute`, and `all`.

```mermaid
sequenceDiagram
    participant Start as DBQueryAPI_get_class_hierarchy_full


    DBQueryAPI_get_class_hierarchy_full->>SessionLocal: calls



    DBQueryAPI_get_class_hierarchy_full->>select: calls



    DBQueryAPI_get_class_hierarchy_full->>join: calls



    DBQueryAPI_get_class_hierarchy_full->>where: calls



    DBQueryAPI_get_class_hierarchy_full->>execute: calls



    DBQueryAPI_get_class_hierarchy_full->>all: calls


```

## Flow from `DBQueryAPI.get_dependency_clusters`

The `get_dependency_clusters` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 1 different components. The primary interactions involve `get_module_structure`.

```mermaid
sequenceDiagram
    participant Start as DBQueryAPI_get_dependency_clusters


    DBQueryAPI_get_dependency_clusters->>get_module_structure: calls


```

## Flow from `J.addOption`

The `addOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `q`, `addOptions`, and `hasOwnProperty`.

```mermaid
sequenceDiagram
    participant Start as J_addOption


    J_addOption->>isArray: calls



    J_addOption->>addOptions: calls



    J_addOption->>q: calls



    J_addOption->>hasOwnProperty: calls



    J_addOption->>trigger: calls


```

## Flow from `J.onFocus`

The `onFocus` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 7 different components. The primary interactions involve `refreshOptions`, `H`, and `showInput`.

```mermaid
sequenceDiagram
    participant Start as J_onFocus


    J_onFocus->>blur: calls



    J_onFocus->>H: calls



    J_onFocus->>preload: calls



    J_onFocus->>trigger: calls



    J_onFocus->>showInput: calls



    J_onFocus->>refreshOptions: calls



    J_onFocus->>refreshState: calls


```

## Flow from `J.selectAll`

The `selectAll` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `hideInput`, `controlChildren`, and `close`.

```mermaid
sequenceDiagram
    participant Start as J_selectAll


    J_selectAll->>controlChildren: calls



    J_selectAll->>hideInput: calls



    J_selectAll->>close: calls



    J_selectAll->>C: calls



    C->>push: calls


```

## Flow from `ModuleGuideGenerator.gather_data`

The `gather_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `module_guide.py`. From there, it coordinates with 1 different components. The primary interactions involve `get_module_structure`.

```mermaid
sequenceDiagram
    participant Start as ModuleGuideGenerator_gather_data


    ModuleGuideGenerator_gather_data->>get_module_structure: calls


```

## Flow from `ProjectMapGenerator.gather_data`

The `gather_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `project_map.py`. From there, it coordinates with 1 different components. The primary interactions involve `get_module_structure`.

```mermaid
sequenceDiagram
    participant Start as ProjectMapGenerator_gather_data


    ProjectMapGenerator_gather_data->>get_module_structure: calls


```

## Flow from `TestCppInheritance.test_inheritance_caller_is_child_class`

The `test_inheritance_caller_is_child_class` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 3 different components. The primary interactions involve `dedent`, `any`, and `_parse`.

```mermaid
sequenceDiagram
    participant Start as TestCppInheritance_test_inheritance_caller_is_child_class


    TestCppInheritance_test_inheritance_caller_is_child_class->>dedent: calls



    TestCppInheritance_test_inheritance_caller_is_child_class->>_parse: calls



    TestCppInheritance_test_inheritance_caller_is_child_class->>any: calls


```

## Flow from `b.getScoreFunction`

The `getScoreFunction` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `prepareSearch` and `_getScoreFunction`.

```mermaid
sequenceDiagram
    participant Start as b_getScoreFunction


    b_getScoreFunction->>prepareSearch: calls



    b_getScoreFunction->>_getScoreFunction: calls


```

## Flow from `highlightFilter`

The `highlightFilter` workflow represents a critical path in the system. When this flow is triggered, execution begins in `utils.js`. From there, it coordinates with 8 different components. The primary interactions involve `toString`, `update`, and `selectNodes`.

```mermaid
sequenceDiagram
    participant Start as highlightFilter


    highlightFilter->>get: calls



    highlightFilter->>includes: calls



    highlightFilter->>toString: calls



    highlightFilter->>push: calls



    highlightFilter->>get: calls



    highlightFilter->>includes: calls



    highlightFilter->>toString: calls



    highlightFilter->>push: calls



    highlightFilter->>push: calls



    highlightFilter->>selectNodes: calls



    selectNodes->>selectNodes: calls



    selectNodes->>filterHighlight: calls



    filterHighlight->>get: calls



    filterHighlight->>hasOwnProperty: calls



    filterHighlight->>push: calls



    filterHighlight->>update: calls



    filterHighlight->>hasOwnProperty: calls



    filterHighlight->>push: calls



    filterHighlight->>update: calls


```

## Flow from `set_sqlite_pragma`

The `set_sqlite_pragma` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 3 different components. The primary interactions involve `close`, `cursor`, and `execute`.

```mermaid
sequenceDiagram
    participant Start as set_sqlite_pragma


    set_sqlite_pragma->>cursor: calls



    set_sqlite_pragma->>execute: calls



    set_sqlite_pragma->>execute: calls



    set_sqlite_pragma->>execute: calls



    set_sqlite_pragma->>execute: calls



    set_sqlite_pragma->>close: calls


```

## Flow from `test_cpp_inline_functions`

The `test_cpp_inline_functions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_cpp.py`. From there, it coordinates with 4 different components. The primary interactions involve `extract_symbols`, `len`, and `set_language`.

```mermaid
sequenceDiagram
    participant Start as test_cpp_inline_functions


    test_cpp_inline_functions->>ASTParser: calls



    test_cpp_inline_functions->>set_language: calls



    test_cpp_inline_functions->>extract_symbols: calls



    test_cpp_inline_functions->>len: calls


```

## Flow from `test_find_callers_of_missing`

The `test_find_callers_of_missing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 3 different components. The primary interactions involve `find_callers_of`, `len`, and `isinstance`.

```mermaid
sequenceDiagram
    participant Start as test_find_callers_of_missing


    test_find_callers_of_missing->>find_callers_of: calls



    test_find_callers_of_missing->>isinstance: calls



    test_find_callers_of_missing->>len: calls


```

## Flow from `test_find_calls_by_missing`

The `test_find_calls_by_missing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 3 different components. The primary interactions involve `find_calls_by`, `len`, and `isinstance`.

```mermaid
sequenceDiagram
    participant Start as test_find_calls_by_missing


    test_find_calls_by_missing->>find_calls_by: calls



    test_find_calls_by_missing->>isinstance: calls



    test_find_calls_by_missing->>len: calls


```

## Flow from `test_js_basic_symbols`

The `test_js_basic_symbols` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_javascript.py`. From there, it coordinates with 5 different components. The primary interactions involve `dedent`, `ASTParser`, and `len`.

```mermaid
sequenceDiagram
    participant Start as test_js_basic_symbols


    test_js_basic_symbols->>ASTParser: calls



    test_js_basic_symbols->>set_language: calls



    test_js_basic_symbols->>dedent: calls



    test_js_basic_symbols->>extract_symbols: calls



    test_js_basic_symbols->>len: calls


```

## Flow from `test_qa_sloppy_shebangs`

The `test_qa_sloppy_shebangs` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_language_qa.py`. From there, it coordinates with 1 different components. The primary interactions involve `detect_language`.

```mermaid
sequenceDiagram
    participant Start as test_qa_sloppy_shebangs


    test_qa_sloppy_shebangs->>detect_language: calls


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*