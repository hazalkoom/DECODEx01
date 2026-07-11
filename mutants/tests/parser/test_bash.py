import pytest
import textwrap
import codelens_core

def test_bash_basic_symbols():
    parser = codelens_core.ASTParser()
    parser.set_language("bash")
    src = textwrap.dedent("""\
        #!/bin/bash
        function deploy_app() {
            echo "Deploying..."
        }
        cleanup() {
            rm -rf /tmp/*
        }
    """)
    symbols = parser.extract_symbols(src)
    assert len(symbols) == 2
    assert symbols[0].name == "deploy_app"
    assert symbols[1].name == "cleanup"

def test_bash_no_dependencies():
    """Prove the engine safely ignores dependencies for Bash."""
    parser = codelens_core.ASTParser()
    parser.set_language("bash")
    src = "source ./config.sh\n. ./utils.sh"
    
    deps = parser.extract_dependencies(src)
    assert deps == []

def test_bash_garbage_safety():
    parser = codelens_core.ASTParser()
    parser.set_language("bash")
    src = "function broken( { echo ' \n rm -rf /"
    symbols = parser.extract_symbols(src)
    assert isinstance(symbols, list)