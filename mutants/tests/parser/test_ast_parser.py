import pytest
import textwrap
import codelens_core

# --- CORE LOGIC TESTS ---
def test_unsupported_language():
    parser = codelens_core.ASTParser()
    assert parser.set_language("cobol") == False

# --- PYTHON QA TESTS ---
def test_python_basic_extraction():
    parser = codelens_core.ASTParser()
    parser.set_language("python")
    src = "import os\nclass User:\n    def login(self): pass"
    
    assert len(parser.extract_symbols(src)) == 2
    assert len(parser.extract_dependencies(src)) == 1

def test_python_relative_and_aliased_imports():
    """Challenge: Can it handle relative dot-imports and 'as' aliases?"""
    parser = codelens_core.ASTParser()
    parser.set_language("python")
    src = textwrap.dedent("""\
        from ..core.models import User as DbUser
        import numpy as np
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 2
    assert deps[0].module_name == "..core.models"
    assert deps[1].module_name == "numpy"

def test_python_multiline_imports():
    """Challenge: Can it extract from formatted multi-line imports?"""
    parser = codelens_core.ASTParser()
    parser.set_language("python")
    src = textwrap.dedent("""\
        from rest_framework.response import (
            Response,
            NotFound
        )
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 1
    assert deps[0].module_name == "rest_framework.response"

def test_python_deeply_nested_symbols():
    """Challenge: Can it find classes and functions buried inside other functions?"""
    parser = codelens_core.ASTParser()
    parser.set_language("python")
    src = textwrap.dedent("""\
        def outer_function():
            import secret_lib
            class InnerClass:
                def inner_method(): pass
    """)
    symbols = parser.extract_symbols(src)
    deps = parser.extract_dependencies(src)
    
    # outer_function, InnerClass, inner_method
    assert len(symbols) == 3
    assert len(deps) == 1
    assert deps[0].module_name == "secret_lib"

def test_python_garbage_safety():
    """Challenge: Ensure parser doesn't crash on syntactically invalid Python"""
    parser = codelens_core.ASTParser()
    parser.set_language("python")
    src = textwrap.dedent("""\
        def broken_func(
        import missing_quote
        class { { {
    """)
    # Should safely return what it can, or empty lists, but NEVER crash
    symbols = parser.extract_symbols(src)
    deps = parser.extract_dependencies(src)
    assert isinstance(symbols, list)
    assert isinstance(deps, list)