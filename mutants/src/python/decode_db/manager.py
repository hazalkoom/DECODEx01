import os
from sqlalchemy import create_engine, insert, select, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from .schema import Base, FileRecord, SymbolRecord, DependencyRecord


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict

# SQLite Performance Tuning: Enable Write-Ahead Logging (WAL) and synchronous optimization
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA synchronous=NORMAL")
    cursor.execute("PRAGMA cache_size=-64000") # 64MB Cache
    cursor.execute("PRAGMA foreign_keys=ON") # Enforce cascade deletes
    cursor.close()
mutants_xǁDBManagerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDBManagerǁget_existing_files__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDBManagerǁremove_stale_files__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDBManagerǁingest_project_data__mutmut: MutantDict = {}  # type: ignore

class DBManager:
    @_mutmut_mutated(mutants_xǁDBManagerǁ__init____mutmut)
    def __init__(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_orig(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_1(self, db_path: str = "XXdecode_graph.dbXX"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_2(self, db_path: str = "DECODE_GRAPH.DB"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_3(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = None
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_4(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(None)
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_5(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = None
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_6(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=None)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(self.engine)
    def xǁDBManagerǁ__init____mutmut_7(self, db_path: str = "decode_graph.db"):
        # We use standard synchronous SQLite for maximum ingestion speed without async overhead
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
        
        # Create all tables if they don't exist
        Base.metadata.create_all(None)

    
    @_mutmut_mutated(mutants_xǁDBManagerǁget_existing_files__mutmut)
    def get_existing_files(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.filepath, FileRecord.last_modified)
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_orig(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.filepath, FileRecord.last_modified)
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_1(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = None
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_2(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(None, FileRecord.last_modified)
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_3(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.filepath, None)
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_4(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.last_modified)
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_5(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.filepath, )
            results = session.execute(stmt).all()
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_6(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.filepath, FileRecord.last_modified)
            results = None
            return {fp: lm for fp, lm in results}

    
    def xǁDBManagerǁget_existing_files__mutmut_7(self) -> dict:
        """Returns a dictionary of {filepath: last_modified_timestamp} for fast lookups."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord.filepath, FileRecord.last_modified)
            results = session.execute(None).all()
            return {fp: lm for fp, lm in results}

    @_mutmut_mutated(mutants_xǁDBManagerǁremove_stale_files__mutmut)
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

    def xǁDBManagerǁremove_stale_files__mutmut_orig(self, filepaths: list):
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

    def xǁDBManagerǁremove_stale_files__mutmut_1(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if filepaths:
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

    def xǁDBManagerǁremove_stale_files__mutmut_2(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(None, len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_3(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, None, 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_4(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), None):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_5(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_6(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_7(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), ):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_8(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(1, len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_9(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1001):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_10(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = None
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_11(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = filepaths[i:i - 1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_12(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = filepaths[i:i+1001]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_13(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(None)
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_14(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(None))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_15(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(None).where(FileRecord.filepath.in_(chunk)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁremove_stale_files__mutmut_16(self, filepaths: list):
        """Deletes specific files. The DB cascade automatically wipes their old symbols and dependencies!"""
        if not filepaths:
            return
        with self.SessionLocal() as session:
            try:
                # Chunking the deletes just in case there are thousands of stale files
                for i in range(0, len(filepaths), 1000):
                    chunk = filepaths[i:i+1000]
                    session.execute(delete(FileRecord).where(FileRecord.filepath.in_(None)))
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    @_mutmut_mutated(mutants_xǁDBManagerǁingest_project_data__mutmut)
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

    def xǁDBManagerǁingest_project_data__mutmut_orig(self, files_data: list, symbols_data: list, deps_data: list):
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

    def xǁDBManagerǁingest_project_data__mutmut_1(self, files_data: list, symbols_data: list, deps_data: list):
        """
        High-performance bulk ingestion of project AST data.
        Takes raw dictionaries to bypass ORM instantiation overhead for mass inserts.
        """
        with self.SessionLocal() as session:
            try:
                # 1. Insert Files
                if files_data:
                    session.execute(None, files_data)
                
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

    def xǁDBManagerǁingest_project_data__mutmut_2(self, files_data: list, symbols_data: list, deps_data: list):
        """
        High-performance bulk ingestion of project AST data.
        Takes raw dictionaries to bypass ORM instantiation overhead for mass inserts.
        """
        with self.SessionLocal() as session:
            try:
                # 1. Insert Files
                if files_data:
                    session.execute(insert(FileRecord), None)
                
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

    def xǁDBManagerǁingest_project_data__mutmut_3(self, files_data: list, symbols_data: list, deps_data: list):
        """
        High-performance bulk ingestion of project AST data.
        Takes raw dictionaries to bypass ORM instantiation overhead for mass inserts.
        """
        with self.SessionLocal() as session:
            try:
                # 1. Insert Files
                if files_data:
                    session.execute(files_data)
                
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

    def xǁDBManagerǁingest_project_data__mutmut_4(self, files_data: list, symbols_data: list, deps_data: list):
        """
        High-performance bulk ingestion of project AST data.
        Takes raw dictionaries to bypass ORM instantiation overhead for mass inserts.
        """
        with self.SessionLocal() as session:
            try:
                # 1. Insert Files
                if files_data:
                    session.execute(insert(FileRecord), )
                
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

    def xǁDBManagerǁingest_project_data__mutmut_5(self, files_data: list, symbols_data: list, deps_data: list):
        """
        High-performance bulk ingestion of project AST data.
        Takes raw dictionaries to bypass ORM instantiation overhead for mass inserts.
        """
        with self.SessionLocal() as session:
            try:
                # 1. Insert Files
                if files_data:
                    session.execute(insert(None), files_data)
                
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

    def xǁDBManagerǁingest_project_data__mutmut_6(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(None, len(symbols_data), 10000):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_7(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, None, 10000):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_8(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, len(symbols_data), None):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_9(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(len(symbols_data), 10000):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_10(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, 10000):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_11(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, len(symbols_data), ):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_12(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(1, len(symbols_data), 10000):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_13(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, len(symbols_data), 10001):
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_14(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(None, symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_15(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(SymbolRecord), None)
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_16(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_17(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(SymbolRecord), )
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_18(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(None), symbols_data[i:i+10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_19(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(SymbolRecord), symbols_data[i:i - 10000])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_20(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(SymbolRecord), symbols_data[i:i+10001])
                
                # 3. Insert Dependencies
                if deps_data:
                    for i in range(0, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_21(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(None, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_22(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, None, 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_23(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, len(deps_data), None):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_24(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_25(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_26(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, len(deps_data), ):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_27(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(1, len(deps_data), 10000):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_28(self, files_data: list, symbols_data: list, deps_data: list):
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
                    for i in range(0, len(deps_data), 10001):
                        session.execute(insert(DependencyRecord), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_29(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(None, deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_30(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(DependencyRecord), None)
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_31(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_32(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(DependencyRecord), )
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_33(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(None), deps_data[i:i+10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_34(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(DependencyRecord), deps_data[i:i - 10000])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    def xǁDBManagerǁingest_project_data__mutmut_35(self, files_data: list, symbols_data: list, deps_data: list):
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
                        session.execute(insert(DependencyRecord), deps_data[i:i+10001])
                        
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

mutants_xǁDBManagerǁ__init____mutmut['_mutmut_orig'] = DBManager.xǁDBManagerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBManagerǁ__init____mutmut['xǁDBManagerǁ__init____mutmut_1'] = DBManager.xǁDBManagerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBManagerǁ__init____mutmut['xǁDBManagerǁ__init____mutmut_2'] = DBManager.xǁDBManagerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBManagerǁ__init____mutmut['xǁDBManagerǁ__init____mutmut_3'] = DBManager.xǁDBManagerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBManagerǁ__init____mutmut['xǁDBManagerǁ__init____mutmut_4'] = DBManager.xǁDBManagerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBManagerǁ__init____mutmut['xǁDBManagerǁ__init____mutmut_5'] = DBManager.xǁDBManagerǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBManagerǁ__init____mutmut['xǁDBManagerǁ__init____mutmut_6'] = DBManager.xǁDBManagerǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDBManagerǁ__init____mutmut['xǁDBManagerǁ__init____mutmut_7'] = DBManager.xǁDBManagerǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁDBManagerǁget_existing_files__mutmut['_mutmut_orig'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBManagerǁget_existing_files__mutmut['xǁDBManagerǁget_existing_files__mutmut_1'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBManagerǁget_existing_files__mutmut['xǁDBManagerǁget_existing_files__mutmut_2'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBManagerǁget_existing_files__mutmut['xǁDBManagerǁget_existing_files__mutmut_3'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBManagerǁget_existing_files__mutmut['xǁDBManagerǁget_existing_files__mutmut_4'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBManagerǁget_existing_files__mutmut['xǁDBManagerǁget_existing_files__mutmut_5'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBManagerǁget_existing_files__mutmut['xǁDBManagerǁget_existing_files__mutmut_6'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDBManagerǁget_existing_files__mutmut['xǁDBManagerǁget_existing_files__mutmut_7'] = DBManager.xǁDBManagerǁget_existing_files__mutmut_7 # type: ignore # mutmut generated

mutants_xǁDBManagerǁremove_stale_files__mutmut['_mutmut_orig'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_1'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_2'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_3'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_4'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_5'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_6'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_7'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_8'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_9'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_10'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_11'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_12'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_13'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_14'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_15'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDBManagerǁremove_stale_files__mutmut['xǁDBManagerǁremove_stale_files__mutmut_16'] = DBManager.xǁDBManagerǁremove_stale_files__mutmut_16 # type: ignore # mutmut generated

mutants_xǁDBManagerǁingest_project_data__mutmut['_mutmut_orig'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_1'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_2'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_3'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_4'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_5'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_6'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_7'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_8'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_9'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_10'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_11'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_12'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_13'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_14'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_15'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_16'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_17'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_18'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_19'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_20'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_21'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_22'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_23'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_24'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_25'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_26'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_27'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_28'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_29'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_30'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_31'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_32'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_32 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_33'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_33 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_34'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_34 # type: ignore # mutmut generated
mutants_xǁDBManagerǁingest_project_data__mutmut['xǁDBManagerǁingest_project_data__mutmut_35'] = DBManager.xǁDBManagerǁingest_project_data__mutmut_35 # type: ignore # mutmut generated