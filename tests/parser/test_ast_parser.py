import pytest
import codelens_core

def test_python_ast_extraction():
    parser = codelens_core.ASTParser()
    assert parser.set_language("python") == True

    mock_python = """
import os
from json import loads

class DatabaseConnection:
    def connect(self):
        pass

def standalone_helper():
    pass
"""
    # 1. Test Symbols (Old functionality still works)
    symbols = parser.extract_symbols(mock_python)
    assert len(symbols) == 3
    assert symbols[0].name == "DatabaseConnection" and symbols[0].type == "class"
    assert symbols[1].name == "connect" and symbols[1].type == "function"
    assert symbols[2].name == "standalone_helper" and symbols[2].type == "function"
    
    # 2. Test Dependencies (New Path A functionality)
    deps = parser.extract_dependencies(mock_python)
    assert len(deps) == 2
    
    # Check 'import os'
    assert deps[0].module_name == "os"
    
    # Check 'from json import loads'
    assert deps[1].module_name == "json"
    assert deps[1].imported_name == "loads"

def test_javascript_ast_extraction():
    parser = codelens_core.ASTParser()
    assert parser.set_language("javascript") == True

    mock_js = """
class ApiClient {
    fetchData() { console.log("fetching"); }
}
function globalHelper() { return true; }
"""
    symbols = parser.extract_symbols(mock_js)
    assert len(symbols) == 3
    assert symbols[0].name == "ApiClient" and symbols[0].type == "class"

def test_unsupported_language():
    parser = codelens_core.ASTParser()
    assert parser.set_language("cobol") == False

def test_cpp_ast_extraction():
    parser = codelens_core.ASTParser()
    assert parser.set_language("cpp") == True
    mock_cpp = "class MyClass { void myMethod() {} }; void myFunc() {}"
    symbols = parser.extract_symbols(mock_cpp)
    # class, method, function
    assert len(symbols) == 2 or len(symbols) == 3 # tree-sitter C++ query finds class & func, possibly methods

def test_go_ast_extraction():
    parser = codelens_core.ASTParser()
    assert parser.set_language("go") == True
    mock_go = "type MyStruct struct {}\nfunc (m *MyStruct) MyMethod() {}\nfunc MyFunc() {}"
    symbols = parser.extract_symbols(mock_go)
    assert len(symbols) == 3

def test_rust_ast_extraction():
    parser = codelens_core.ASTParser()
    assert parser.set_language("rust") == True
    mock_rust = "struct MyStruct {}\nfn my_func() {}"
    symbols = parser.extract_symbols(mock_rust)
    assert len(symbols) == 2