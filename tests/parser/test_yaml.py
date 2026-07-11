import pytest
import codelens_core

def test_yaml_safely_ignored():
    """Prove YAML is safely parsed but returns empty structural lists."""
    parser = codelens_core.ASTParser()
    parser.set_language("yaml")
    
    src = "version: '3'\nservices:\n  web:\n    image: nginx"
    
    symbols = parser.extract_symbols(src)
    deps = parser.extract_dependencies(src)
    
    assert symbols == []
    assert deps == []

def test_yaml_garbage_safety():
    parser = codelens_core.ASTParser()
    parser.set_language("yaml")
    src = "version: '3'\n  broken_indent: \n - mapping"
    assert isinstance(parser.extract_symbols(src), list)