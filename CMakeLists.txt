cmake_minimum_required(VERSION 3.15)
project(DECODEx01Core C CXX)

include(FetchContent)

# --- 1. CORE ENGINE ---
FetchContent_Declare(
    tree-sitter
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter.git
    GIT_TAG v0.24.6
)
FetchContent_GetProperties(tree-sitter)
if(NOT tree-sitter_POPULATED)
    FetchContent_Populate(tree-sitter)
endif()

# --- 2. PROGRAMMING LANGUAGES ---
# Python
FetchContent_Declare(
    tree-sitter-python
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-python.git
    GIT_TAG v0.23.5
)
FetchContent_GetProperties(tree-sitter-python)
if(NOT tree-sitter-python_POPULATED)
    FetchContent_Populate(tree-sitter-python)
endif()

# JavaScript
FetchContent_Declare(
    tree-sitter-javascript
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-javascript.git
    GIT_TAG v0.23.1
)
FetchContent_GetProperties(tree-sitter-javascript)
if(NOT tree-sitter-javascript_POPULATED)
    FetchContent_Populate(tree-sitter-javascript)
endif()

# C++
FetchContent_Declare(
    tree-sitter-cpp
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-cpp.git
    GIT_TAG v0.23.4
)
FetchContent_GetProperties(tree-sitter-cpp)
if(NOT tree-sitter-cpp_POPULATED)
    FetchContent_Populate(tree-sitter-cpp)
endif()

# Go
FetchContent_Declare(
    tree-sitter-go
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-go.git
    GIT_TAG v0.23.4
)
FetchContent_GetProperties(tree-sitter-go)
if(NOT tree-sitter-go_POPULATED)
    FetchContent_Populate(tree-sitter-go)
endif()

# Rust
FetchContent_Declare(
    tree-sitter-rust
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-rust.git
    GIT_TAG v0.23.2
)
FetchContent_GetProperties(tree-sitter-rust)
if(NOT tree-sitter-rust_POPULATED)
    FetchContent_Populate(tree-sitter-rust)
endif()

# --- 3. CONFIG & SCRIPTING LANGUAGES ---
# Bash
FetchContent_Declare(
    tree-sitter-bash
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-bash.git
    GIT_TAG v0.23.3
)
FetchContent_GetProperties(tree-sitter-bash)
if(NOT tree-sitter-bash_POPULATED)
    FetchContent_Populate(tree-sitter-bash)
endif()

# JSON
FetchContent_Declare(
    tree-sitter-json
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-json.git
    GIT_TAG v0.24.8
)
FetchContent_GetProperties(tree-sitter-json)
if(NOT tree-sitter-json_POPULATED)
    FetchContent_Populate(tree-sitter-json)
endif()

# YAML
FetchContent_Declare(
    tree-sitter-yaml
    GIT_REPOSITORY https://github.com/ikatyang/tree-sitter-yaml.git
    GIT_TAG v0.5.0
)
FetchContent_GetProperties(tree-sitter-yaml)
if(NOT tree-sitter-yaml_POPULATED)
    FetchContent_Populate(tree-sitter-yaml)
endif()


# --- 4. COMPILE EVERYTHING ---
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(codelens_core 
    src/api/bindings.cpp 
    src/core/fs_walker.cpp 
    src/core/language_detector.cpp
    src/parser/ast_parser.cpp 
    src/parser/symbol_extractor.cpp
    src/parser/dependency_extractor.cpp
    
    # Core
    ${tree-sitter_SOURCE_DIR}/lib/src/lib.c
    
    # Language Parsers (C Files)
    ${tree-sitter-python_SOURCE_DIR}/src/parser.c
    ${tree-sitter-python_SOURCE_DIR}/src/scanner.c
    
    ${tree-sitter-javascript_SOURCE_DIR}/src/parser.c
    ${tree-sitter-javascript_SOURCE_DIR}/src/scanner.c
    
    # The C++ Scanner extension fix! (.c instead of .cc)
    ${tree-sitter-cpp_SOURCE_DIR}/src/parser.c
    ${tree-sitter-cpp_SOURCE_DIR}/src/scanner.c
    
    ${tree-sitter-go_SOURCE_DIR}/src/parser.c
    
    ${tree-sitter-rust_SOURCE_DIR}/src/parser.c
    ${tree-sitter-rust_SOURCE_DIR}/src/scanner.c
    
    ${tree-sitter-bash_SOURCE_DIR}/src/parser.c
    ${tree-sitter-bash_SOURCE_DIR}/src/scanner.c
    
    ${tree-sitter-json_SOURCE_DIR}/src/parser.c
    
    ${tree-sitter-yaml_SOURCE_DIR}/src/parser.c
    ${tree-sitter-yaml_SOURCE_DIR}/src/scanner.cc
)

# THE HEADER COLLISION FIX: Only include the master Tree-sitter core rulebook!
target_include_directories(codelens_core PRIVATE 
    ${tree-sitter_SOURCE_DIR}/lib/include
    ${tree-sitter_SOURCE_DIR}/lib/src
    ${CMAKE_CURRENT_SOURCE_DIR}/src/core
    ${CMAKE_CURRENT_SOURCE_DIR}/src/parser
    ${CMAKE_CURRENT_SOURCE_DIR}/src/api
)

# Source-specific include path for tree-sitter-yaml to find its vendored
# <tree_sitter/parser.h> without globally polluting include paths for other grammars
set_source_files_properties(
    ${tree-sitter-yaml_SOURCE_DIR}/src/parser.c
    ${tree-sitter-yaml_SOURCE_DIR}/src/scanner.cc
    PROPERTIES INCLUDE_DIRECTORIES "${tree-sitter-yaml_SOURCE_DIR}/src"
)

install(TARGETS codelens_core DESTINATION .)