import pytest
from python.decode_db.manager import DBManager
from python.decode_db.query_api import DBQueryAPI

@pytest.fixture
def temp_db_path(tmp_path):
    """Provides a temporary, isolated SQLite database file path for each test."""
    db_file = tmp_path / "test_decode_graph.db"
    return str(db_file)

@pytest.fixture
def db_manager(temp_db_path):
    """Provides an isolated DBManager instance connected to the temporary DB."""
    # SQLite uses the file if it exists, or creates it.
    manager = DBManager(db_path=temp_db_path)
    return manager

@pytest.fixture
def db_query(temp_db_path, db_manager):
    """Provides an isolated DBQueryAPI connected to the same temporary DB."""
    return DBQueryAPI(db_path=temp_db_path)

@pytest.fixture
def populated_db(db_manager, db_query):
    """Provides a DB populated with a basic set of data for query tests."""
    files_data = [
        {"filepath": "/test/app.py", "language": "python", "last_modified": 12345.0},
        {"filepath": "/test/utils.py", "language": "python", "last_modified": 12346.0}
    ]
    
    symbols_data = [
        {
            "file_id": 1, 
            "name": "AppServer", 
            "fully_qualified_name": "app.AppServer",
            "signature": "AppServer",
            "return_type": "AppServer",
            "type": "class", 
            "docstring": "Main app server class",
            "start_line": 10, 
            "end_line": 50
        },
        {
            "file_id": 1, 
            "name": "start", 
            "fully_qualified_name": "app.AppServer.start",
            "signature": "start(self, port)",
            "return_type": "None",
            "type": "function", 
            "docstring": "Start the server",
            "start_line": 12, 
            "end_line": 20
        },
        {
            "file_id": 2, 
            "name": "helper_func", 
            "fully_qualified_name": "utils.helper_func",
            "signature": "helper_func()",
            "return_type": "int",
            "type": "function", 
            "docstring": "A helper function",
            "start_line": 5, 
            "end_line": 8
        }
    ]
    
    deps_data = [
        {"file_id": 1, "module_name": "os", "imported_name": None, "line_number": 1},
        {"file_id": 1, "module_name": "pytest", "imported_name": "fixture", "line_number": 2},
        {"file_id": 2, "module_name": "sys", "imported_name": "exit", "line_number": 1}
    ]

    refs_data = [
        {"file_id": 1, "caller_fqn": "app.AppServer.start", "callee_fqn": "utils.helper_func", "kind": "Call", "line_number": 15},
        {"file_id": 2, "caller_fqn": "utils.helper_func", "callee_fqn": "os.path.join", "kind": "Call", "line_number": 6},
        {"file_id": 1, "caller_fqn": "AppServer", "callee_fqn": "BaseServer", "kind": "Inheritance", "line_number": 10},
    ]
    
    db_manager.ingest_project_data(files_data, symbols_data, deps_data, refs_data)
    
    return db_manager, db_query
