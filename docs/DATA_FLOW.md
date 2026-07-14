# Data Flow
> **Onboarding question:** How does information move?


## Workflow: main

The `main` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_main.cpp`. From there, it coordinates with 82 different components. The primary interactions involve `lstrip`, `exists`, and `connect`.

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

The `get_domain_entities` workflow represents a critical path in the system. When this flow is triggered, execution begins in `query_api.py`. From there, it coordinates with 11 different components. The primary interactions involve `join`, `query`, and `SessionLocal`.

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

The `setup` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 57 different components. The primary interactions involve `create`, `updateOriginalInput`, and `P`.

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

The `setupOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 3 different components. The primary interactions involve `addOptions`, `y`, and `registerOptionGroup`.

```mermaid
graph TD
    Start[J_setupOptions]


    J_setupOptions --> addOptions



    J_setupOptions --> y



    J_setupOptions --> registerOptionGroup


```

## Workflow: J.setupTemplates

The `setupTemplates` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 73 different components. The primary interactions involve `Eu`, `pg`, and `_create`.

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

## Workflow: ArchitectureGenerator.gather_data

The `gather_data` workflow represents a critical path in the system. When this flow is triggered, execution begins in `architecture.py`. From there, it coordinates with 2 different components. The primary interactions involve `get_module_structure` and `get_cross_module_edges`.

```mermaid
graph TD
    Start[ArchitectureGenerator_gather_data]


    ArchitectureGenerator_gather_data --> get_module_structure



    ArchitectureGenerator_gather_data --> get_cross_module_edges


```

## Workflow: BaseGenerator._generate_ai_summary

The `_generate_ai_summary` workflow represents a critical path in the system. When this flow is triggered, execution begins in `base_generator.py`. From there, it coordinates with 6 different components. The primary interactions involve `create`, `strip`, and `dumps`.

```mermaid
graph TD
    Start[BaseGenerator__generate_ai_summary]


    BaseGenerator__generate_ai_summary --> getenv



    BaseGenerator__generate_ai_summary --> print



    BaseGenerator__generate_ai_summary --> getenv



    BaseGenerator__generate_ai_summary --> OpenAI



    BaseGenerator__generate_ai_summary --> print



    BaseGenerator__generate_ai_summary --> create



    BaseGenerator__generate_ai_summary --> dumps



    BaseGenerator__generate_ai_summary --> strip



    BaseGenerator__generate_ai_summary --> print


```

## Workflow: DocsCoordinator.generate_all

The `generate_all` workflow represents a critical path in the system. When this flow is triggered, execution begins in `coordinator.py`. From there, it coordinates with 3 different components. The primary interactions involve `generate`, `makedirs`, and `_render_index`.

```mermaid
graph TD
    Start[DocsCoordinator_generate_all]


    DocsCoordinator_generate_all --> makedirs



    DocsCoordinator_generate_all --> generate



    DocsCoordinator_generate_all --> _render_index


```

## Workflow: Ey

The `Ey` workflow represents a critical path in the system. When this flow is triggered, execution begins in `vis-network.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `create` and `qv`.

```mermaid
graph TD
    Start[Ey]


    Ey --> create



    Ey --> qv


```

## Workflow: J.addOption

The `addOption` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 5 different components. The primary interactions involve `q`, `trigger`, and `addOptions`.

```mermaid
graph TD
    Start[J_addOption]


    J_addOption --> isArray



    J_addOption --> addOptions



    J_addOption --> q



    J_addOption --> hasOwnProperty



    J_addOption --> trigger


```

## Workflow: J.advanceSelection

The `advanceSelection` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 8 different components. The primary interactions involve `getLastActive`, `K`, and `setActiveItemClass`.

```mermaid
graph TD
    Start[J_advanceSelection]


    J_advanceSelection --> inputValue



    J_advanceSelection --> K



    J_advanceSelection --> K



    J_advanceSelection --> getLastActive



    J_advanceSelection --> contains



    J_advanceSelection --> getAdjacent



    J_advanceSelection --> contains



    J_advanceSelection --> removeActiveItem



    J_advanceSelection --> setActiveItemClass



    J_advanceSelection --> moveCaret


```

## Workflow: J.clearOptions

The `clearOptions` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 4 different components. The primary interactions involve `trigger`, `y`, and `clearCache`.

```mermaid
graph TD
    Start[J_clearOptions]


    J_clearOptions --> clearCache



    J_clearOptions --> y



    J_clearOptions --> indexOf



    J_clearOptions --> trigger


```

## Workflow: J.getScoreFunction

The `getScoreFunction` workflow represents a critical path in the system. When this flow is triggered, execution begins in `tom-select.complete.min.js`. From there, it coordinates with 2 different components. The primary interactions involve `getSearchOptions` and `getScoreFunction`.

```mermaid
graph TD
    Start[J_getScoreFunction]


    J_getScoreFunction --> getScoreFunction



    J_getScoreFunction --> getSearchOptions


```

## Workflow: TestPythonInheritance.test_single_inheritance_detected

The `test_single_inheritance_detected` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_inheritance.py`. From there, it coordinates with 3 different components. The primary interactions involve `dedent`, `_parse`, and `len`.

```mermaid
graph TD
    Start[TestPythonInheritance_test_single_inheritance_detected]


    TestPythonInheritance_test_single_inheritance_detected --> dedent



    TestPythonInheritance_test_single_inheritance_detected --> _parse



    TestPythonInheritance_test_single_inheritance_detected --> len


```

## Workflow: language_repo

The `language_repo` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_language_detector.py`. From there, it coordinates with 2 different components. The primary interactions involve `write_text` and `str`.

```mermaid
graph TD
    Start[language_repo]


    language_repo --> write_text



    language_repo --> write_text



    language_repo --> write_text



    language_repo --> write_text



    language_repo --> write_text



    language_repo --> write_text



    language_repo --> str



    language_repo --> str



    language_repo --> str



    language_repo --> str



    language_repo --> str



    language_repo --> str


```

## Workflow: test_find_symbol_missing

The `test_find_symbol_missing` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_query_api.py`. From there, it coordinates with 3 different components. The primary interactions involve `find_symbol`, `isinstance`, and `len`.

```mermaid
graph TD
    Start[test_find_symbol_missing]


    test_find_symbol_missing --> find_symbol



    test_find_symbol_missing --> isinstance



    test_find_symbol_missing --> len


```

## Workflow: test_get_existing_files

The `test_get_existing_files` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_manager.py`. From there, it coordinates with 3 different components. The primary interactions involve `len`, `isinstance`, and `get_existing_files`.

```mermaid
graph TD
    Start[test_get_existing_files]


    test_get_existing_files --> get_existing_files



    test_get_existing_files --> isinstance



    test_get_existing_files --> len


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

The `test_python_garbage_safety` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_ast_parser.py`. From there, it coordinates with 6 different components. The primary interactions involve `isinstance`, `dedent`, and `ASTParser`.

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

## Workflow: test_walker_nonexistent_directory

The `test_walker_nonexistent_directory` workflow represents a critical path in the system. When this flow is triggered, execution begins in `test_fs_walker.py`. From there, it coordinates with 2 different components. The primary interactions involve `walk_repository` and `len`.

```mermaid
graph TD
    Start[test_walker_nonexistent_directory]


    test_walker_nonexistent_directory --> walk_repository



    test_walker_nonexistent_directory --> len


```


---
*Generated by DECODE NLG | [← Back to Index](index.md)*