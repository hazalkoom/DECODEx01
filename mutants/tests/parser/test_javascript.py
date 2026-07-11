import pytest
import textwrap
import codelens_core

def test_js_basic_symbols():
    """Test basic JS class and function extraction."""
    parser = codelens_core.ASTParser()
    parser.set_language("javascript")
    src = textwrap.dedent("""\
        class ApiClient {
            fetchData() { console.log("fetching"); }
        }
        function globalHelper() { return true; }
    """)
    symbols = parser.extract_symbols(src)
    assert len(symbols) == 3
    assert symbols[0].name == "ApiClient"

def test_js_es6_imports():
    """Challenge: Destructured ES6 imports."""
    parser = codelens_core.ASTParser()
    parser.set_language("javascript")
    src = textwrap.dedent("""\
        import React, { useState, useEffect } from 'react';
        import { merge } from 'lodash';
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 2
    assert deps[0].module_name == "'react'"
    assert deps[1].module_name == "'lodash'"

def test_js_side_effect_imports():
    """Challenge: Side-effect imports that don't bind to variables."""
    parser = codelens_core.ASTParser()
    parser.set_language("javascript")
    src = "import 'dotenv/config';\nimport './styles.css';"
    deps = parser.extract_dependencies(src)
    assert len(deps) == 2
    assert deps[0].module_name == "'dotenv/config'"
    assert deps[1].module_name == "'./styles.css'"

def test_js_es6_exports():
    """Challenge: Re-exporting from other files (Dependency Edge)."""
    parser = codelens_core.ASTParser()
    parser.set_language("javascript")
    src = textwrap.dedent("""\
        export { Button } from './components/Button';
        export * from './utils/math';
    """)
    deps = parser.extract_dependencies(src)
    assert len(deps) == 2
    assert deps[0].module_name == "'./components/Button'"
    assert deps[1].module_name == "'./utils/math'"

def test_js_garbage_safety():
    """Challenge: Don't crash on invalid JS."""
    parser = codelens_core.ASTParser()
    parser.set_language("javascript")
    src = "import { missing from 'broken\n class { fn() { "
    deps = parser.extract_dependencies(src)
    symbols = parser.extract_symbols(src)
    assert isinstance(deps, list)
    assert isinstance(symbols, list)