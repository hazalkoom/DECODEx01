import pytest

def test_find_symbol_success(populated_db):
    """Test finding a specific class or function symbol."""
    _, db_query = populated_db
    
    results = db_query.find_symbol("AppServer")
    assert len(results) == 1
    assert results[0]["file"] == "/test/app.py"
    assert results[0]["type"] == "class"
    assert results[0]["line"] == 10
    
    results_func = db_query.find_symbol("start")
    assert len(results_func) == 1
    assert results_func[0]["type"] == "function"

def test_find_symbol_missing(db_query):
    """Edge Case: Test finding a symbol that doesn't exist."""
    results = db_query.find_symbol("NonExistent")
    assert isinstance(results, list)
    assert len(results) == 0

def test_find_files_importing_success(populated_db):
    """Test querying who imports a specific library."""
    _, db_query = populated_db
    
    # Exact match
    results = db_query.find_files_importing("pytest")
    assert len(results) == 1
    assert results[0]["file"] == "/test/app.py"
    assert results[0]["imported_name"] == "fixture"
    
    # Partial match using .like()
    results_partial = db_query.find_files_importing("ys")
    assert len(results_partial) == 1
    assert results_partial[0]["file"] == "/test/utils.py"

def test_find_files_importing_missing(db_query):
    """Edge Case: Test querying imports for an unknown library."""
    results = db_query.find_files_importing("unknown_lib")
    assert isinstance(results, list)
    assert len(results) == 0

def test_get_file_outline_success(populated_db):
    """Test getting all symbols scoped to a file."""
    _, db_query = populated_db
    
    results = db_query.get_file_outline("app.py")
    assert len(results) == 2
    
    # Sort to ensure consistent checking
    results_sorted = sorted(results, key=lambda x: x["line"])
    
    assert results_sorted[0]["name"] == "AppServer"
    assert results_sorted[0]["type"] == "class"
    assert results_sorted[1]["name"] == "start"
    assert results_sorted[1]["type"] == "function"

def test_get_file_outline_missing(db_query):
    """Edge Case: Test getting outline for file that doesn't exist."""
    results = db_query.get_file_outline("missing.py")
    assert isinstance(results, list)
    assert len(results) == 0
