from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from .schema import FileRecord, SymbolRecord, DependencyRecord


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDBQueryAPIǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDBQueryAPIǁfind_symbol__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDBQueryAPIǁget_file_outline__mutmut: MutantDict = {}  # type: ignore

class DBQueryAPI:
    @_mutmut_mutated(mutants_xǁDBQueryAPIǁ__init____mutmut)
    def __init__(self, db_path: str = "decode_graph.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
    def xǁDBQueryAPIǁ__init____mutmut_orig(self, db_path: str = "decode_graph.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
    def xǁDBQueryAPIǁ__init____mutmut_1(self, db_path: str = "XXdecode_graph.dbXX"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
    def xǁDBQueryAPIǁ__init____mutmut_2(self, db_path: str = "DECODE_GRAPH.DB"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)
    def xǁDBQueryAPIǁ__init____mutmut_3(self, db_path: str = "decode_graph.db"):
        self.engine = None
        self.SessionLocal = sessionmaker(bind=self.engine)
    def xǁDBQueryAPIǁ__init____mutmut_4(self, db_path: str = "decode_graph.db"):
        self.engine = create_engine(None)
        self.SessionLocal = sessionmaker(bind=self.engine)
    def xǁDBQueryAPIǁ__init____mutmut_5(self, db_path: str = "decode_graph.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = None
    def xǁDBQueryAPIǁ__init____mutmut_6(self, db_path: str = "decode_graph.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=None)

    @_mutmut_mutated(mutants_xǁDBQueryAPIǁfind_symbol__mutmut)
    def find_symbol(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_orig(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_1(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = None
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_2(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(None)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_3(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(None).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_4(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(None, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_5(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, None).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_6(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_7(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, ).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_8(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name != symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_9(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = None
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_10(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(None).all()
            
            return [
                {"file": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_11(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"XXfileXX": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_12(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"FILE": f.filepath, "type": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_13(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "XXtypeXX": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_14(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "TYPE": s.type, "line": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_15(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "XXlineXX": s.start_line} 
                for s, f in results
            ]

    def xǁDBQueryAPIǁfind_symbol__mutmut_16(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            # Join Symbols with Files so we know exactly which file it lives in
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "type": s.type, "LINE": s.start_line} 
                for s, f in results
            ]

    @_mutmut_mutated(mutants_xǁDBQueryAPIǁfind_files_importing__mutmut)
    def find_files_importing(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_orig(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_1(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = None
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_2(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                None
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_3(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(None).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_4(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(None, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_5(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, None).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_6(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_7(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, ).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_8(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(None)
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_9(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = None
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_10(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(None).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_11(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"XXfileXX": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_12(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"FILE": f.filepath, "line": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_13(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "XXlineXX": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_14(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "LINE": d.line_number, "imported_name": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_15(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "XXimported_nameXX": d.imported_name} 
                for f, d in results
            ]
            

    def xǁDBQueryAPIǁfind_files_importing__mutmut_16(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            # We use .like() to catch partial matches (e.g., 'tree_sitter/api.h')
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            
            return [
                {"file": f.filepath, "line": d.line_number, "IMPORTED_NAME": d.imported_name} 
                for f, d in results
            ]
            
    @_mutmut_mutated(mutants_xǁDBQueryAPIǁget_file_outline__mutmut)
    def get_file_outline(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_orig(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_1(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = None
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_2(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(None)
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_3(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(None).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_4(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(None).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_5(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(None))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_6(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = None
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_7(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(None).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_8(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"XXnameXX": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_9(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"NAME": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_10(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "XXtypeXX": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_11(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "TYPE": s.type, "line": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_12(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "XXlineXX": s.start_line} 
                for s in results
            ]
    def xǁDBQueryAPIǁget_file_outline__mutmut_13(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "LINE": s.start_line} 
                for s in results
            ]

mutants_xǁDBQueryAPIǁ__init____mutmut['_mutmut_orig'] = DBQueryAPI.xǁDBQueryAPIǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁ__init____mutmut['xǁDBQueryAPIǁ__init____mutmut_1'] = DBQueryAPI.xǁDBQueryAPIǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁ__init____mutmut['xǁDBQueryAPIǁ__init____mutmut_2'] = DBQueryAPI.xǁDBQueryAPIǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁ__init____mutmut['xǁDBQueryAPIǁ__init____mutmut_3'] = DBQueryAPI.xǁDBQueryAPIǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁ__init____mutmut['xǁDBQueryAPIǁ__init____mutmut_4'] = DBQueryAPI.xǁDBQueryAPIǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁ__init____mutmut['xǁDBQueryAPIǁ__init____mutmut_5'] = DBQueryAPI.xǁDBQueryAPIǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁ__init____mutmut['xǁDBQueryAPIǁ__init____mutmut_6'] = DBQueryAPI.xǁDBQueryAPIǁ__init____mutmut_6 # type: ignore # mutmut generated

mutants_xǁDBQueryAPIǁfind_symbol__mutmut['_mutmut_orig'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_1'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_2'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_3'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_4'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_5'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_6'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_7'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_8'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_9'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_10'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_11'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_12'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_13'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_14'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_15'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_symbol__mutmut['xǁDBQueryAPIǁfind_symbol__mutmut_16'] = DBQueryAPI.xǁDBQueryAPIǁfind_symbol__mutmut_16 # type: ignore # mutmut generated

mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['_mutmut_orig'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_1'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_2'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_3'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_4'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_5'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_6'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_7'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_8'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_9'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_10'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_11'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_12'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_13'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_14'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_15'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁfind_files_importing__mutmut['xǁDBQueryAPIǁfind_files_importing__mutmut_16'] = DBQueryAPI.xǁDBQueryAPIǁfind_files_importing__mutmut_16 # type: ignore # mutmut generated

mutants_xǁDBQueryAPIǁget_file_outline__mutmut['_mutmut_orig'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_1'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_2'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_3'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_4'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_5'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_6'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_7'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_8'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_9'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_10'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_11'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_12'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDBQueryAPIǁget_file_outline__mutmut['xǁDBQueryAPIǁget_file_outline__mutmut_13'] = DBQueryAPI.xǁDBQueryAPIǁget_file_outline__mutmut_13 # type: ignore # mutmut generated