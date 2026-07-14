# Call Flow
> **Onboarding question:** What happens during execution?


## Flow from `main`

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `Network`, `first`, and `in_`.

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

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `any`, `SessionLocal`, and `join`.

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

The `onClick` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `clearActiveItems`, `focus`, and `blur`.

```mermaid
sequenceDiagram
    participant Start as J_onClick


    J_onClick->>clearActiveItems: calls



    J_onClick->>focus: calls



    J_onClick->>blur: calls



    J_onClick->>focus: calls


```

## Flow from `J.setup`

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 58 different components. The primary interactions involve `preload`, `onFocus`, and `stopPropagation`.

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

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `registerOptionGroup`, `y`, and `addOptions`.

```mermaid
sequenceDiagram
    participant Start as J_setupOptions


    J_setupOptions->>addOptions: calls



    J_setupOptions->>y: calls



    J_setupOptions->>registerOptionGroup: calls


```

## Flow from `J.setupTemplates`

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 77 different components. The primary interactions involve `assign`, `Hv`, and `Yd`.

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

The `test_schema_setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 5 different components. The primary interactions involve `len`, `select`, and `SessionLocal`.

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

## Flow from `DBManager.ingest_project_data`

The `ingest_project_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 7 different components. The primary interactions involve `len`, `SessionLocal`, and `execute`.

```mermaid
sequenceDiagram
    participant Start as DBManager_ingest_project_data


    DBManager_ingest_project_data->>SessionLocal: calls



    DBManager_ingest_project_data->>execute: calls



    DBManager_ingest_project_data->>insert: calls



    DBManager_ingest_project_data->>range: calls



    DBManager_ingest_project_data->>len: calls



    DBManager_ingest_project_data->>execute: calls



    DBManager_ingest_project_data->>insert: calls



    DBManager_ingest_project_data->>range: calls



    DBManager_ingest_project_data->>len: calls



    DBManager_ingest_project_data->>execute: calls



    DBManager_ingest_project_data->>insert: calls



    DBManager_ingest_project_data->>range: calls



    DBManager_ingest_project_data->>len: calls



    DBManager_ingest_project_data->>execute: calls



    DBManager_ingest_project_data->>insert: calls



    DBManager_ingest_project_data->>commit: calls



    DBManager_ingest_project_data->>rollback: calls


```

## Flow from `DBQueryAPI.find_files_importing`

The `find_files_importing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 7 different components. The primary interactions involve `select`, `where`, and `SessionLocal`.

```mermaid
sequenceDiagram
    participant Start as DBQueryAPI_find_files_importing


    DBQueryAPI_find_files_importing->>SessionLocal: calls



    DBQueryAPI_find_files_importing->>select: calls



    DBQueryAPI_find_files_importing->>join: calls



    DBQueryAPI_find_files_importing->>where: calls



    DBQueryAPI_find_files_importing->>like: calls



    DBQueryAPI_find_files_importing->>execute: calls



    DBQueryAPI_find_files_importing->>all: calls


```

## Flow from `DBQueryAPI.get_class_hierarchy`

The `get_class_hierarchy` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 6 different components. The primary interactions involve `select`, `where`, and `SessionLocal`.

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

## Flow from `J.addOptionGroup`

The `addOptionGroup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `registerOptionGroup` and `trigger`.

```mermaid
sequenceDiagram
    participant Start as J_addOptionGroup


    J_addOptionGroup->>registerOptionGroup: calls



    J_addOptionGroup->>trigger: calls


```

## Flow from `J.clearActiveItems`

The `clearActiveItems` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `S`.

```mermaid
sequenceDiagram
    participant Start as J_clearActiveItems


    J_clearActiveItems->>S: calls


```

## Flow from `J.clearOptions`

The `clearOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `clearCache`, `y`, and `trigger`.

```mermaid
sequenceDiagram
    participant Start as J_clearOptions


    J_clearOptions->>clearCache: calls



    J_clearOptions->>y: calls



    J_clearOptions->>indexOf: calls



    J_clearOptions->>trigger: calls


```

## Flow from `J.destroy`

The `destroy` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `trigger`, `_destroy`, and `off`.

```mermaid
sequenceDiagram
    participant Start as J_destroy


    J_destroy->>trigger: calls



    J_destroy->>off: calls



    J_destroy->>remove: calls



    J_destroy->>remove: calls



    J_destroy->>S: calls



    J_destroy->>_destroy: calls


```

## Flow from `J.onInput`

The `onInput` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `trigger`, `load`, and `refreshOptions`.

```mermaid
sequenceDiagram
    participant Start as J_onInput


    J_onInput->>inputValue: calls



    J_onInput->>call: calls



    J_onInput->>load: calls



    J_onInput->>refreshOptions: calls



    J_onInput->>trigger: calls


```

## Flow from `J.selectable`

The `selectable` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `querySelectorAll`.

```mermaid
sequenceDiagram
    participant Start as J_selectable


    J_selectable->>querySelectorAll: calls


```

## Flow from `J.setActiveItemClass`

The `setActiveItemClass` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 6 different components. The primary interactions involve `trigger`, `push`, and `querySelector`.

```mermaid
sequenceDiagram
    participant Start as J_setActiveItemClass


    J_setActiveItemClass->>querySelector: calls



    J_setActiveItemClass->>S: calls



    J_setActiveItemClass->>C: calls



    J_setActiveItemClass->>trigger: calls



    J_setActiveItemClass->>indexOf: calls



    J_setActiveItemClass->>push: calls



    C->>push: calls


```

## Flow from `J.uncacheValue`

The `uncacheValue` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `remove` and `getOption`.

```mermaid
sequenceDiagram
    participant Start as J_uncacheValue


    J_uncacheValue->>getOption: calls



    J_uncacheValue->>remove: calls


```

## Flow from `TestCppReturnTypes.test_bool_return_type`

The `test_bool_return_type` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_return_types.py`. From there, it coordinates with 1 different components. The primary interactions involve `_parse`.

```mermaid
sequenceDiagram
    participant Start as TestCppReturnTypes_test_bool_return_type


    TestCppReturnTypes_test_bool_return_type->>_parse: calls


```

## Flow from `qg`

The `qg` workflow represents a critical path in the system. When this flow is triggered, execution begins in `vis-network.min.js`. From there, it coordinates with 10 different components. The primary interactions involve `mg`, `jg`, and `push`.

```mermaid
sequenceDiagram
    participant Start as qg


    qg->>jg: calls



    qg->>jg: calls



    qg->>filter: calls



    qg->>mg: calls



    qg->>push: calls



    qg->>Rg: calls



    qg->>concat: calls



    jg->>call: calls



    Rg->>Ig: calls



    Rg->>push: calls



    Rg->>sort: calls



    Rg->>sort: calls



    Ig->>indexOf: calls


```

## Flow from `test_bash_basic_symbols`

The `test_bash_basic_symbols` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_bash.py`. From there, it coordinates with 5 different components. The primary interactions involve `len`, `ASTParser`, and `dedent`.

```mermaid
sequenceDiagram
    participant Start as test_bash_basic_symbols


    test_bash_basic_symbols->>ASTParser: calls



    test_bash_basic_symbols->>set_language: calls



    test_bash_basic_symbols->>dedent: calls



    test_bash_basic_symbols->>extract_symbols: calls



    test_bash_basic_symbols->>len: calls


```

## Flow from `test_get_class_hierarchy_success`

The `test_get_class_hierarchy_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 2 different components. The primary interactions involve `len` and `get_class_hierarchy`.

```mermaid
sequenceDiagram
    participant Start as test_get_class_hierarchy_success


    test_get_class_hierarchy_success->>get_class_hierarchy: calls



    test_get_class_hierarchy_success->>len: calls


```

## Flow from `test_get_file_outline_success`

The `test_get_file_outline_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api.py`. From there, it coordinates with 3 different components. The primary interactions involve `len`, `get_file_outline`, and `sorted`.

```mermaid
sequenceDiagram
    participant Start as test_get_file_outline_success


    test_get_file_outline_success->>get_file_outline: calls



    test_get_file_outline_success->>len: calls



    test_get_file_outline_success->>sorted: calls


```

## Flow from `test_js_es6_exports`

The `test_js_es6_exports` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_javascript.py`. From there, it coordinates with 5 different components. The primary interactions involve `len`, `ASTParser`, and `extract_dependencies`.

```mermaid
sequenceDiagram
    participant Start as test_js_es6_exports


    test_js_es6_exports->>ASTParser: calls



    test_js_es6_exports->>set_language: calls



    test_js_es6_exports->>dedent: calls



    test_js_es6_exports->>extract_dependencies: calls



    test_js_es6_exports->>len: calls


```

## Flow from `test_remove_stale_files_cascade`

The `test_remove_stale_files_cascade` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 7 different components. The primary interactions involve `len`, `SessionLocal`, and `first`.

```mermaid
sequenceDiagram
    participant Start as test_remove_stale_files_cascade


    test_remove_stale_files_cascade->>SessionLocal: calls



    test_remove_stale_files_cascade->>query: calls



    test_remove_stale_files_cascade->>count: calls



    test_remove_stale_files_cascade->>query: calls



    test_remove_stale_files_cascade->>count: calls



    test_remove_stale_files_cascade->>query: calls



    test_remove_stale_files_cascade->>count: calls



    test_remove_stale_files_cascade->>remove_stale_files: calls



    test_remove_stale_files_cascade->>SessionLocal: calls



    test_remove_stale_files_cascade->>query: calls



    test_remove_stale_files_cascade->>count: calls



    test_remove_stale_files_cascade->>query: calls



    test_remove_stale_files_cascade->>first: calls



    test_remove_stale_files_cascade->>query: calls



    test_remove_stale_files_cascade->>all: calls



    test_remove_stale_files_cascade->>len: calls



    test_remove_stale_files_cascade->>query: calls



    test_remove_stale_files_cascade->>all: calls



    test_remove_stale_files_cascade->>len: calls



    test_remove_stale_files_cascade->>query: calls


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*