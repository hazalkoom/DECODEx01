import pytest
from sqlalchemy.exc import IntegrityError
from python.decode_db.schema import FileRecord, SymbolRecord, DependencyRecord
from sqlalchemy import select

def test_schema_setup(db_manager):
    """Test that all tables are correctly created by the manager initialization."""
    with db_manager.SessionLocal() as session:
        # If the tables don't exist, these queries will throw OperationalError
        files = session.execute(select(FileRecord)).all()
        symbols = session.execute(select(SymbolRecord)).all()
        deps = session.execute(select(DependencyRecord)).all()
        
        assert len(files) == 0
        assert len(symbols) == 0
        assert len(deps) == 0

def test_bulk_ingestion(db_manager):
    """Test that ingest_project_data properly loads mass dictionaries into SQLite."""
    files_data = [{"filepath": "/test/a.py", "language": "python", "last_modified": 1.0}]
    symbols_data = [{"file_id": 1, "name": "ClassA", "type": "class", "start_line": 1, "end_line": 10}]
    deps_data = [{"file_id": 1, "module_name": "os", "imported_name": None, "line_number": 2}]
    
    db_manager.ingest_project_data(files_data, symbols_data, deps_data)
    
    with db_manager.SessionLocal() as session:
        assert session.query(FileRecord).count() == 1
        assert session.query(SymbolRecord).count() == 1
        assert session.query(DependencyRecord).count() == 1

def test_get_existing_files(populated_db):
    """Test retrieving existing files logic."""
    db_manager, _ = populated_db
    
    existing = db_manager.get_existing_files()
    assert isinstance(existing, dict)
    assert len(existing) == 2
    assert existing["/test/app.py"] == 12345.0
    assert existing["/test/utils.py"] == 12346.0

def test_remove_stale_files_cascade(populated_db):
    """Test incremental deletion. Crucial: cascade must wipe child records."""
    db_manager, _ = populated_db
    
    # Pre-check child counts
    with db_manager.SessionLocal() as session:
        assert session.query(SymbolRecord).count() == 3
        assert session.query(DependencyRecord).count() == 3
        
    # Delete ONE file (/test/app.py which is file_id 1)
    db_manager.remove_stale_files(["/test/app.py"])
    
    with db_manager.SessionLocal() as session:
        # File 1 is gone, File 2 remains
        assert session.query(FileRecord).count() == 1
        assert session.query(FileRecord).first().filepath == "/test/utils.py"
        
        # All symbols and deps for File 1 must be cascade deleted!
        symbols = session.query(SymbolRecord).all()
        assert len(symbols) == 1
        assert symbols[0].name == "helper_func" # from File 2
        
        deps = session.query(DependencyRecord).all()
        assert len(deps) == 1
        assert deps[0].module_name == "sys" # from File 2

def test_empty_ingestions(db_manager):
    """Edge Case: Ensure manager doesn't crash on empty arrays."""
    try:
        db_manager.ingest_project_data([], [], [])
        db_manager.remove_stale_files([])
    except Exception as e:
        pytest.fail(f"Empty data arrays caused an unexpected exception: {e}")

def test_duplicate_filepath_insertion(db_manager):
    """Edge Case: DB should prevent inserting duplicate filepaths."""
    files_data = [
        {"filepath": "/test/dup.py", "language": "python", "last_modified": 1.0},
        {"filepath": "/test/dup.py", "language": "python", "last_modified": 2.0}
    ]
    
    with pytest.raises(IntegrityError):
        db_manager.ingest_project_data(files_data, [], [])
