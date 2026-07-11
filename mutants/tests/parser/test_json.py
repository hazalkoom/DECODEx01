import pytest
import codelens_core

def test_json_safely_ignored():
    """Prove JSON is safely parsed but returns empty structural lists."""
    parser = codelens_core.ASTParser()
    parser.set_language("json")
    
    src = '{"name": "decode", "version": "1.0", "dependencies": {"react": "^18.0"}}'
    
    symbols = parser.extract_symbols(src)
    deps = parser.extract_dependencies(src)
    
    # JSON has no functions/classes or imports in the AST definition
    assert symbols == []
    assert deps == []

def test_json_garbage_safety():
    parser = codelens_core.ASTParser()
    parser.set_language("json")
    src = '{"broken": [1, 2, }'
    assert isinstance(parser.extract_symbols(src), list)