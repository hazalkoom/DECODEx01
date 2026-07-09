import pytest
import codelens_core

def test_python_ast_extraction():
    parser = codelens_core.ASTParser()
    assert parser.set_language("python") == True, "Failed to load Python grammar"

    mock_python = """
class DatabaseConnection:
    def connect(self):
        pass

def standalone_helper():
    pass
"""
    symbols = parser.parse_code(mock_python)
    assert len(symbols) == 3
    assert symbols[0].name == "DatabaseConnection" and symbols[0].type == "class"
    assert symbols[1].name == "connect" and symbols[1].type == "function"
    assert symbols[2].name == "standalone_helper" and symbols[2].type == "function"


def test_javascript_ast_extraction():
    parser = codelens_core.ASTParser()
    assert parser.set_language("javascript") == True, "Failed to load JS grammar"

    mock_js = """
class ApiClient {
    fetchData() {
        console.log("fetching");
    }
}

function globalHelper() {
    return true;
}
"""
    symbols = parser.parse_code(mock_js)
    assert len(symbols) == 3
    
    # Check JS extraction
    assert symbols[0].name == "ApiClient" and symbols[0].type == "class"
    assert symbols[1].name == "fetchData" and symbols[1].type == "function"
    assert symbols[2].name == "globalHelper" and symbols[2].type == "function"

def test_unsupported_language():
    parser = codelens_core.ASTParser()
    # Engine should safely reject languages it doesn't know yet
    assert parser.set_language("cobol") == False