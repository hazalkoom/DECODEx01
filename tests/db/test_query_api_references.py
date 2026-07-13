"""
tests/db/test_query_api_references.py
Phase 1D: Tests for the three new DBQueryAPI methods:
  - find_callers_of(symbol_name)
  - find_calls_by(symbol_name)
  - get_class_hierarchy()
"""


def test_find_callers_of_success(populated_db):
    """find_callers_of should return who calls the given function."""
    _, db_query = populated_db

    results = db_query.find_callers_of("utils.helper_func")
    assert len(results) == 1
    assert results[0]["caller"] == "app.AppServer.start"
    assert results[0]["kind"] == "Call"


def test_find_callers_of_multiple(populated_db):
    """os.path.join is called by helper_func — verify the lookup works."""
    _, db_query = populated_db

    results = db_query.find_callers_of("os.path.join")
    assert len(results) == 1
    assert results[0]["caller"] == "utils.helper_func"


def test_find_callers_of_missing(populated_db):
    """Symbol with no callers should return an empty list."""
    _, db_query = populated_db

    results = db_query.find_callers_of("nonexistent_function")
    assert isinstance(results, list)
    assert len(results) == 0


def test_find_calls_by_success(populated_db):
    """find_calls_by should return what the given symbol calls."""
    _, db_query = populated_db

    results = db_query.find_calls_by("app.AppServer.start")
    assert len(results) == 1
    assert results[0]["callee"] == "utils.helper_func"
    assert results[0]["kind"] == "Call"


def test_find_calls_by_missing(populated_db):
    """Symbol that calls nothing should return empty list."""
    _, db_query = populated_db

    results = db_query.find_calls_by("nonexistent_caller")
    assert isinstance(results, list)
    assert len(results) == 0


def test_find_callers_excludes_inheritance(populated_db):
    """find_callers_of should NOT return Inheritance references (kind filter)."""
    _, db_query = populated_db

    # BaseServer appears as an Inheritance callee, not a Call callee
    results = db_query.find_callers_of("BaseServer")
    assert len(results) == 0  # Filtered out because kind != 'Call'


def test_get_class_hierarchy_success(populated_db):
    """get_class_hierarchy should return all Inheritance references."""
    _, db_query = populated_db

    results = db_query.get_class_hierarchy()
    assert len(results) == 1
    assert results[0]["child_class"] == "AppServer"
    assert results[0]["parent_class"] == "BaseServer"
    assert results[0]["file"] == "/test/app.py"


def test_get_class_hierarchy_empty_db(db_query):
    """An empty DB should return an empty hierarchy list."""
    results = db_query.get_class_hierarchy()
    assert isinstance(results, list)
    assert len(results) == 0


def test_reference_has_file_and_line(populated_db):
    """All reference results should contain file path and line number."""
    _, db_query = populated_db

    callers = db_query.find_callers_of("utils.helper_func")
    assert "file" in callers[0]
    assert "line" in callers[0]
    assert callers[0]["line"] == 15

    hierarchy = db_query.get_class_hierarchy()
    assert "file" in hierarchy[0]
    assert "line" in hierarchy[0]
    assert hierarchy[0]["line"] == 10
