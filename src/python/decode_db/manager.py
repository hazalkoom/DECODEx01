import os
from sqlalchemy import create_engine, insert, select, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from .schema import Base, FileRecord, SymbolRecord, DependencyRecord

# SQLite Performance Tuning: Enable Write-Ahead Logging (WAL) and synchronous optimization
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA synchronous=NORMAL")
    cursor.execute("PRAGMA cache_size=-64000") # 64MB Cache
    cursor.close()

class DBManager:
    def __init__(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)

    
    def get_existing_files(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.filepath, FileRecord.last_modified)
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    def remove_stale_files(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def ingest_project_data(self, files_data: list, symbols_data: list, deps_data: list):
        """
        High-performance bulk ingestion of project AST data.
        Takes raw dictionaries to bypass ORM instantiation overhead for mass inserts.
        """
        with self.SessionLocal() as session:
            try:
                # 1. Insert Files
                if files_data:
                    session.execute(insert(FileRecord), files_data)
                
                # 2. Insert Symbols
                if symbols_data:
                    # chunking helps SQLite not run out of memory during massive inserts
                    for i in range(0, len(symbols_data), 10000):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e