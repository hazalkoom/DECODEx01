# Call Flow
> **Onboarding question:** What happens during execution?


## Flow from `main`

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `Session`, `write`, and `Network`.

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

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `defaultdict`, `any`, and `filter`.

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

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 58 different components. The primary interactions involve `enable`, `removeEventListener`, and `v`.

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

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 77 different components. The primary interactions involve `forEach`, `configureKeyboardBindings`, and `destroy`.

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

## Flow from `DBManager.ingest_project_data`

The `ingest_project_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `manager.py`. From there, it coordinates with 7 different components. The primary interactions involve `commit`, `SessionLocal`, and `execute`.

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

## Flow from `DocsCoordinator.generate_all`

The `generate_all` workflow represents a critical path in the system. When this flow is triggered, execution begins in `coordinator.py`. From there, it coordinates with 3 different components. The primary interactions involve `makedirs`, `_render_index`, and `generate`.

```mermaid
sequenceDiagram
    participant Start as DocsCoordinator_generate_all


    DocsCoordinator_generate_all->>makedirs: calls



    DocsCoordinator_generate_all->>generate: calls



    DocsCoordinator_generate_all->>_render_index: calls


```

## Flow from `J.canCreate`

The `canCreate` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `call`.

```mermaid
sequenceDiagram
    participant Start as J_canCreate


    J_canCreate->>call: calls


```

## Flow from `J.clearActiveItems`

The `clearActiveItems` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 1 different components. The primary interactions involve `S`.

```mermaid
sequenceDiagram
    participant Start as J_clearActiveItems


    J_clearActiveItems->>S: calls


```

## Flow from `J.controlChildren`

The `controlChildren` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `from` and `querySelectorAll`.

```mermaid
sequenceDiagram
    participant Start as J_controlChildren


    J_controlChildren->>from: calls



    J_controlChildren->>querySelectorAll: calls


```

## Flow from `J.inputState`

The `inputState` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `setTextboxValue`, `toggle`, and `contains`.

```mermaid
sequenceDiagram
    participant Start as J_inputState


    J_inputState->>contains: calls



    J_inputState->>P: calls



    J_inputState->>setTextboxValue: calls



    J_inputState->>P: calls



    J_inputState->>toggle: calls


```

## Flow from `J.o`

The `o` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `w`, `N`, and `append`.

```mermaid
sequenceDiagram
    participant Start as J_o


    J_o->>w: calls



    J_o->>N: calls



    J_o->>N: calls



    J_o->>append: calls



    J_o->>push: calls


```

## Flow from `J.onPaste`

The `onPaste` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 9 different components. The primary interactions involve `H`, `y`, and `inputValue`.

```mermaid
sequenceDiagram
    participant Start as J_onPaste


    J_onPaste->>isFull: calls



    J_onPaste->>H: calls



    J_onPaste->>setTimeout: calls



    J_onPaste->>inputValue: calls



    J_onPaste->>match: calls



    J_onPaste->>trim: calls



    J_onPaste->>split: calls



    J_onPaste->>y: calls



    J_onPaste->>createItem: calls


```

## Flow from `J.removeItem`

The `removeItem` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 14 different components. The primary interactions involve `positionDropdown`, `hasOwnProperty`, and `L`.

```mermaid
sequenceDiagram
    participant Start as J_removeItem


    J_removeItem->>getItem: calls



    J_removeItem->>L: calls



    J_removeItem->>remove: calls



    J_removeItem->>contains: calls



    J_removeItem->>indexOf: calls



    J_removeItem->>splice: calls



    J_removeItem->>S: calls



    J_removeItem->>splice: calls



    J_removeItem->>hasOwnProperty: calls



    J_removeItem->>removeOption: calls



    J_removeItem->>setCaret: calls



    J_removeItem->>updateOriginalInput: calls



    J_removeItem->>refreshState: calls



    J_removeItem->>positionDropdown: calls



    J_removeItem->>trigger: calls


```

## Flow from `J.selectAll`

The `selectAll` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `hideInput`, `close`, and `C`.

```mermaid
sequenceDiagram
    participant Start as J_selectAll


    J_selectAll->>controlChildren: calls



    J_selectAll->>hideInput: calls



    J_selectAll->>close: calls



    J_selectAll->>C: calls



    C->>push: calls


```

## Flow from `TestCppReturnTypes._parse`

The `_parse` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_return_types.py`. From there, it coordinates with 3 different components. The primary interactions involve `analyze_file`, `ASTParser`, and `set_language`.

```mermaid
sequenceDiagram
    participant Start as TestCppReturnTypes__parse


    TestCppReturnTypes__parse->>ASTParser: calls



    TestCppReturnTypes__parse->>set_language: calls



    TestCppReturnTypes__parse->>analyze_file: calls


```

## Flow from `b.getSortFunction`

The `getSortFunction` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `_getSortFunction` and `prepareSearch`.

```mermaid
sequenceDiagram
    participant Start as b_getSortFunction


    b_getSortFunction->>prepareSearch: calls



    b_getSortFunction->>_getSortFunction: calls


```

## Flow from `test_cpp_nested_namespaces`

The `test_cpp_nested_namespaces` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_cpp.py`. From there, it coordinates with 5 different components. The primary interactions involve `dedent`, `extract_symbols`, and `ASTParser`.

```mermaid
sequenceDiagram
    participant Start as test_cpp_nested_namespaces


    test_cpp_nested_namespaces->>ASTParser: calls



    test_cpp_nested_namespaces->>set_language: calls



    test_cpp_nested_namespaces->>dedent: calls



    test_cpp_nested_namespaces->>extract_symbols: calls



    test_cpp_nested_namespaces->>len: calls


```

## Flow from `test_find_calls_by_success`

The `test_find_calls_by_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api_references.py`. From there, it coordinates with 2 different components. The primary interactions involve `find_calls_by` and `len`.

```mermaid
sequenceDiagram
    participant Start as test_find_calls_by_success


    test_find_calls_by_success->>find_calls_by: calls



    test_find_calls_by_success->>len: calls


```

## Flow from `test_find_files_importing_success`

The `test_find_files_importing_success` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api.py`. From there, it coordinates with 2 different components. The primary interactions involve `len` and `find_files_importing`.

```mermaid
sequenceDiagram
    participant Start as test_find_files_importing_success


    test_find_files_importing_success->>find_files_importing: calls



    test_find_files_importing_success->>len: calls



    test_find_files_importing_success->>find_files_importing: calls



    test_find_files_importing_success->>len: calls


```

## Flow from `test_json_safely_ignored`

The `test_json_safely_ignored` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_json.py`. From there, it coordinates with 4 different components. The primary interactions involve `extract_symbols`, `ASTParser`, and `set_language`.

```mermaid
sequenceDiagram
    participant Start as test_json_safely_ignored


    test_json_safely_ignored->>ASTParser: calls



    test_json_safely_ignored->>set_language: calls



    test_json_safely_ignored->>extract_symbols: calls



    test_json_safely_ignored->>extract_dependencies: calls


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*