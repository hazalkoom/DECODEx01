# Mad-Lib style templates for different sections

TPL_PROJECT_OVERVIEW = """This repository is built primarily using {primary_language}. It is a medium-to-large sized project consisting of {file_count} files, {class_count} classes, and {function_count} functions. At its core, the project heavily relies on external libraries like {top_deps} to manage its underlying operations. Execution typically begins at {entry_points}, which serve as the primary entry points into the system."""

TPL_IMPORTANT_FILES_INTRO = """When diving into this codebase, you shouldn't try to read everything at once. The most critical file to understand first is `{top_file}`. It acts as a {top_role}—meaning almost every other part of the system interacts with it. Once you understand that, look at `{second_file}`, which serves as a {second_role}."""

TPL_IMPORTANT_FILE_DETAIL = """The file `{filepath}` is crucial because it functions as a {role}. It has {in_degree} other components depending on it, and it orchestrates {out_degree} different downstream tasks."""

TPL_CALL_FLOW = """The `{ep_name}` workflow represents a critical path in the system. When this flow is triggered, execution begins in `{ep_file}`. From there, it coordinates with {num_components} different components. The primary interactions involve {key_callees}."""

TPL_DATA_MODEL = """The domain model of this application is centered around several core entities. The most heavily referenced concept is `{top_entity}`, which acts as a {top_role} and provides {method_count} methods. It is closely followed by `{second_entity}`."""

TPL_ARCHITECTURE = """The architecture of this system is divided into several major modules. The most central module is `{central_module}`, containing {central_files} files. Communication generally flows across {edges_count} different module boundaries."""

TPL_MODULE_GUIDE = """The `{module_name}` module is responsible for grouping related functionality. It contains {total_files} files and defines {total_symbols} core symbols."""

TPL_DEPENDENCY_GUIDE = """The dependency graph shows how different parts of the system interact. A strong connection exists between `{source_module}` and `{target_module}`, with {edge_count} direct interactions."""

TPL_READING_GUIDE = """Your reading journey should begin with `{top_file}`. This file provides the foundation. After mastering that, progress to `{second_file}` to understand how the core logic is applied."""

TPL_PROJECT_MAP = """The project directory structure is designed to separate concerns. In the `{module_path}` directory, you will find {file_count} files primarily written in {languages}."""

TPL_GLOSSARY = """The term `{term_name}` is a critical concept defined in `{file_path}`. It is referenced {ref_count} times throughout the codebase. {docstring}"""
