from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from .schema import FileRecord, SymbolRecord, DependencyRecord, ReferenceRecord

class DBQueryAPI:
    def __init__(self, db_path: str = "decode_graph.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)

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
            
    def get_file_outline(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            
            return [
                {"name": s.name, "type": s.type, "line": s.start_line} 
                for s in results
            ]

    def find_callers_of(self, symbol_name: str) -> list:
        """Find all functions/methods that call a given symbol (reverse call graph lookup)."""
        with self.SessionLocal() as session:
            stmt = (
                select(ReferenceRecord, FileRecord)
                .join(FileRecord)
                .where(ReferenceRecord.callee_fqn == symbol_name)
                .where(ReferenceRecord.kind == "Call")
            )
            results = session.execute(stmt).all()
            return [
                {
                    "caller": r.caller_fqn,
                    "file": f.filepath,
                    "line": r.line_number,
                    "kind": r.kind
                }
                for r, f in results
            ]

    def find_calls_by(self, symbol_name: str) -> list:
        """Find all functions/methods called by a given symbol (forward call graph lookup)."""
        with self.SessionLocal() as session:
            stmt = (
                select(ReferenceRecord, FileRecord)
                .join(FileRecord)
                .where(ReferenceRecord.caller_fqn == symbol_name)
                .where(ReferenceRecord.kind == "Call")
            )
            results = session.execute(stmt).all()
            return [
                {
                    "callee": r.callee_fqn,
                    "file": f.filepath,
                    "line": r.line_number,
                    "kind": r.kind
                }
                for r, f in results
            ]

    def get_class_hierarchy(self) -> list:
        """Return all class inheritance relationships in the project (child -> parent)."""
        with self.SessionLocal() as session:
            stmt = (
                select(ReferenceRecord, FileRecord)
                .join(FileRecord)
                .where(ReferenceRecord.kind == "Inheritance")
            )
            results = session.execute(stmt).all()
            return [
                {
                    "child_class": r.caller_fqn,
                    "parent_class": r.callee_fqn,
                    "file": f.filepath,
                    "line": r.line_number
                }
                for r, f in results
            ]