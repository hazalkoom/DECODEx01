import pytest
import textwrap
import codelens_core

def test_go_basic_symbols():
    parser = codelens_core.ASTParser()
    parser.set_language("go")
    src = textwrap.dedent("""\
        type Server struct {}
        func (s *Server) Start() {}
        func standalone() {}
    """)
    symbols = parser.extract_symbols(src)
    assert len(symbols) == 3
    assert symbols[0].name == "Server"
    assert symbols[1].name == "Start"

def test_go_grouped_imports():
    """Challenge: Go uses grouped imports inside parentheses."""
    parser = codelens_core.ASTParser()
    parser.set_language("go")
    src = textwrap.dedent("""\
        import (
            "fmt"
            "net/http"
            myfmt "custom/fmt"
        )
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 3
    assert deps[0].module_name == '"fmt"'
    assert deps[1].module_name == '"net/http"'
    assert deps[2].module_name == '"custom/fmt"'

def test_go_garbage_safety():
    parser = codelens_core.ASTParser()
    parser.set_language("go")
    src = "import ( \"broken \n func ( { "
    deps = parser.extract_dependencies(src)
    assert isinstance(deps, list)