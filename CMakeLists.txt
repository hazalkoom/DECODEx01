cmake_minimum_required(VERSION 3.15)
project(DECODEx01Core C CXX) # Note: Added 'C' because tree-sitter is written in C

# 1. Download Tree-sitter Core and Python Grammar directly from GitHub
include(FetchContent)

FetchContent_Declare(
    tree-sitter
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter.git
    GIT_TAG v0.24.6
)
# Only fetch the source — we compile lib.c directly, so skip its CMake build.
FetchContent_GetProperties(tree-sitter)
if(NOT tree-sitter_POPULATED)
    FetchContent_Populate(tree-sitter)
endif()

FetchContent_Declare(
    tree-sitter-python
    GIT_REPOSITORY https://github.com/tree-sitter/tree-sitter-python.git
    GIT_TAG v0.23.5
)
# Only fetch the source — we compile parser.c/scanner.c directly.
# Using FetchContent_MakeAvailable here would invoke its own CMakeLists.txt,
# which tries to regenerate parser.c using the tree-sitter CLI (not installed).
FetchContent_GetProperties(tree-sitter-python)
if(NOT tree-sitter-python_POPULATED)
    FetchContent_Populate(tree-sitter-python)
endif()

# 2. Find pybind11
find_package(pybind11 CONFIG REQUIRED)

# 3. Create our Python module
# We now include the tree-sitter C files directly in our compilation!
pybind11_add_module(codelens_core 
    src/bindings.cpp 
    src/fs_walker.cpp 
    src/language_detector.cpp
    
    # We will create these two files in the next step
    src/ast_parser.cpp 
    
    # Compile the Tree-sitter C files directly into our module
    ${tree-sitter_SOURCE_DIR}/lib/src/lib.c
    ${tree-sitter-python_SOURCE_DIR}/src/parser.c
    ${tree-sitter-python_SOURCE_DIR}/src/scanner.c
)

# 4. Tell the compiler where to find the header files
target_include_directories(codelens_core PRIVATE 
    ${tree-sitter_SOURCE_DIR}/lib/include
    ${tree-sitter_SOURCE_DIR}/lib/src
    ${tree-sitter-python_SOURCE_DIR}/src
)

install(TARGETS codelens_core DESTINATION .)