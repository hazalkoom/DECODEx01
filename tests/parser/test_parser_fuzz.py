import pytest
from hypothesis import given, strategies as st, settings, HealthCheck
import codelens_core

# List of supported languages
SUPPORTED_LANGUAGES = ["python", "javascript", "cpp", "go", "rust", "bash", "json", "yaml"]

@settings(suppress_health_check=[HealthCheck.too_slow], deadline=None)
@given(
    lang=st.sampled_from(SUPPORTED_LANGUAGES),
    src=st.text(min_size=0, max_size=10000)
)
def test_ast_parser_fuzz(lang, src):
    """
    Fuzz test for AST parser: feed arbitrary unicode/ASCII strings to extract_symbols
    and extract_dependencies. The parser should never crash or raise C++ exceptions.
    """
    parser = codelens_core.ASTParser()
    assert parser.set_language(lang) is True
    
    # We don't care about the returned value, we only care that it does not crash/throw.
    try:
        symbols = parser.extract_symbols(src)
        assert isinstance(symbols, list)
    except Exception as e:
        pytest.fail(f"extract_symbols crashed with exception: {e} for language {lang}")

    try:
        deps = parser.extract_dependencies(src)
        assert isinstance(deps, list)
    except Exception as e:
        pytest.fail(f"extract_dependencies crashed with exception: {e} for language {lang}")

@settings(suppress_health_check=[HealthCheck.too_slow], deadline=None)
@given(
    garbage_lang=st.text(min_size=0, max_size=100)
)
def test_set_language_garbage(garbage_lang):
    """
    Ensure the parser rejects unsupported/garbage language names gracefully.
    """
    parser = codelens_core.ASTParser()
    # It must return False and not crash/leak.
    assert parser.set_language(garbage_lang) is False
