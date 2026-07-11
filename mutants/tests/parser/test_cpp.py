import pytest
import textwrap
import codelens_core

def test_cpp_dogfooding_extraction():
    """Our original dogfooding test for the ASTParser header."""
    parser = codelens_core.ASTParser()
    parser.set_language("cpp")
    src = textwrap.dedent("""\
        #pragma once
        #include <string>
        #include <vector>
        #include <tree_sitter/api.h>
        #include "../core/ast_types.hpp"
        class ASTParser { TSParser* parser; };
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 4
    assert deps[0].module_name == "<string>"
    assert deps[3].module_name == '"../core/ast_types.hpp"'

def test_cpp_macro_guarded_includes():
    """Challenge: Can it find includes hidden behind preprocessor macros?"""
    parser = codelens_core.ASTParser()
    parser.set_language("cpp")
    src = textwrap.dedent("""\
        #ifdef _WIN32
            #include <windows.h>
        #else
            #include <unistd.h>
        #endif
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 2
    assert deps[0].module_name == "<windows.h>"
    assert deps[1].module_name == "<unistd.h>"

def test_cpp_weird_spacing():
    """Challenge: C++ allows absurd spacing. Does Tree-sitter catch it?"""
    parser = codelens_core.ASTParser()
    parser.set_language("cpp")
    src = "#   include      <iostream>\n#include\"local.h\""
    deps = parser.extract_dependencies(src)
    assert len(deps) == 2
    assert deps[0].module_name == "<iostream>"
    assert deps[1].module_name == '"local.h"'

def test_cpp_nested_namespaces():
    """Challenge: Extracting symbols across nested namespaces and structs."""
    parser = codelens_core.ASTParser()
    parser.set_language("cpp")
    src = textwrap.dedent("""\
        namespace Core {
            namespace Utils {
                class Logger { void log() {} };
                struct DataNode {};
            }
        }
    """)
    symbols = parser.extract_symbols(src)
    # class Logger, void log()
    # Note: Structs aren't in our current symbol_query_str for C++, 
    # so we expect exactly 2 symbols to prove the query is strictly obeyed.
    assert len(symbols) == 2
    assert symbols[0].name == "Logger"

def test_cpp_inline_functions():
    """Challenge: Can it extract raw standalone functions?"""
    parser = codelens_core.ASTParser()
    parser.set_language("cpp")
    src = "inline void fast_math() {} \n static int add(int a, int b) { return a+b; }"
    symbols = parser.extract_symbols(src)
    assert len(symbols) == 2
    assert symbols[0].name == "fast_math"
    assert symbols[1].name == "add"