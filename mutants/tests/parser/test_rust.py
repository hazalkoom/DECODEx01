import pytest
import textwrap
import codelens_core

def test_rust_basic_symbols():
    parser = codelens_core.ASTParser()
    parser.set_language("rust")
    src = textwrap.dedent("""\
        struct Connection {}
        fn establish() {}
    """)
    symbols = parser.extract_symbols(src)
    assert len(symbols) == 2
    assert symbols[0].name == "Connection"

def test_rust_nested_imports():
    """Challenge: Rust allows highly nested use statements."""
    parser = codelens_core.ASTParser()
    parser.set_language("rust")
    src = textwrap.dedent("""\
        use std::fs;
        use std::collections::{HashMap, HashSet};
        use std::io::Result as IoResult;
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 3
    assert deps[0].module_name == "std::fs"
    # The Tree-sitter (_) wildcard gracefully captures the entire nested block!
    assert deps[1].module_name == "std::collections::{HashMap, HashSet}"
    assert deps[2].module_name == "std::io::Result as IoResult"

def test_rust_garbage_safety():
    parser = codelens_core.ASTParser()
    parser.set_language("rust")
    src = "use std:: \n struct { fn { "
    deps = parser.extract_dependencies(src)
    assert isinstance(deps, list)