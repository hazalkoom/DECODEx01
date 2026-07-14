from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from collections import defaultdict
from typing import List, Dict, Any
from .schema import FileRecord, SymbolRecord, DependencyRecord, ReferenceRecord

class DBQueryAPI:
    def __init__(self, db_path: str = "decode_graph.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        self.SessionLocal = sessionmaker(bind=self.engine)

    def find_symbol(self, symbol_name: str):
        """Find everywhere a specific class or function is defined."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord, FileRecord).join(FileRecord).where(SymbolRecord.name == symbol_name)
            results = session.execute(stmt).all()
            return [{"file": f.filepath, "type": s.type, "line": s.start_line} for s, f in results]

    def find_files_importing(self, module_name: str):
        """Find all files that import a specific library (e.g., 'pytest' or 'sqlalchemy')."""
        with self.SessionLocal() as session:
            stmt = select(FileRecord, DependencyRecord).join(DependencyRecord).where(
                DependencyRecord.module_name.like(f"%{module_name}%")
            )
            results = session.execute(stmt).all()
            return [{"file": f.filepath, "line": d.line_number, "imported_name": d.imported_name} for f, d in results]
            
    def get_file_outline(self, filename: str):
        """Get all classes and functions defined inside a specific file."""
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord).join(FileRecord).where(FileRecord.filepath.like(f"%{filename}%"))
            results = session.execute(stmt).scalars().all()
            return [{"name": s.name, "type": s.type, "line": s.start_line} for s in results]

    def find_callers_of(self, symbol_name: str) -> list:
        """Find all functions/methods that call a given symbol (reverse call graph lookup)."""
        with self.SessionLocal() as session:
            stmt = select(ReferenceRecord, FileRecord).join(FileRecord).where(ReferenceRecord.callee_fqn == symbol_name).where(ReferenceRecord.kind == "Call")
            results = session.execute(stmt).all()
            return [{"caller": r.caller_fqn, "file": f.filepath, "line": r.line_number, "kind": r.kind} for r, f in results]

    def find_calls_by(self, symbol_name: str) -> list:
        """Find all functions/methods called by a given symbol (forward call graph lookup)."""
        with self.SessionLocal() as session:
            stmt = select(ReferenceRecord, FileRecord).join(FileRecord).where(ReferenceRecord.caller_fqn == symbol_name).where(ReferenceRecord.kind == "Call")
            results = session.execute(stmt).all()
            return [{"callee": r.callee_fqn, "file": f.filepath, "line": r.line_number, "kind": r.kind} for r, f in results]

    def get_class_hierarchy(self) -> list:
        """Return all class inheritance relationships in the project (child -> parent)."""
        with self.SessionLocal() as session:
            stmt = select(ReferenceRecord, FileRecord).join(FileRecord).where(ReferenceRecord.kind == "Inheritance")
            results = session.execute(stmt).all()
            return [{"child_class": r.caller_fqn, "parent_class": r.callee_fqn, "file": f.filepath, "line": r.line_number} for r, f in results]

    # --- New Methods for Documentation Generation ---

    def get_all_files(self) -> List[Dict]:
        with self.SessionLocal() as session:
            files = session.query(FileRecord).all()
            return [{"filepath": f.filepath, "language": f.language, "symbol_count": len(f.symbols), "dep_count": len(f.dependencies), "ref_count": len(f.references)} for f in files]

    def get_all_symbols(self) -> List[Dict]:
        with self.SessionLocal() as session:
            stmt = select(SymbolRecord, FileRecord).join(FileRecord)
            results = session.execute(stmt).all()
            return [{"name": s.name, "fqn": s.fully_qualified_name, "type": s.type, "file": f.filepath, "signature": s.signature, "return_type": s.return_type, "docstring": s.docstring, "start_line": s.start_line, "end_line": s.end_line} for s, f in results]

    def get_all_dependencies(self) -> List[Dict]:
        with self.SessionLocal() as session:
            stmt = select(DependencyRecord, FileRecord).join(FileRecord)
            results = session.execute(stmt).all()
            return [{"file": f.filepath, "module_name": d.module_name, "imported_name": d.imported_name, "line": d.line_number} for d, f in results]

    def get_all_references(self) -> List[Dict]:
        with self.SessionLocal() as session:
            stmt = select(ReferenceRecord, FileRecord).join(FileRecord)
            results = session.execute(stmt).all()
            return [{"caller_fqn": r.caller_fqn, "callee_fqn": r.callee_fqn, "kind": r.kind, "file": f.filepath, "line": r.line_number} for r, f in results]

    def get_file_importance_scores(self) -> List[Dict]:
        with self.SessionLocal() as session:
            files = session.query(FileRecord).all()
            scores = []
            
            # Precompute in/out degrees for FQNs
            fqn_to_file = {}
            for f in files:
                for s in f.symbols:
                    if s.fully_qualified_name:
                        fqn_to_file[s.fully_qualified_name] = f.filepath
                        
            in_degrees = defaultdict(int)
            out_degrees = defaultdict(int)
            
            refs = session.query(ReferenceRecord).all()
            for r in refs:
                if r.callee_fqn in fqn_to_file:
                    in_degrees[fqn_to_file[r.callee_fqn]] += 1
                if r.caller_fqn in fqn_to_file:
                    out_degrees[fqn_to_file[r.caller_fqn]] += 1
                    
            dep_counts = defaultdict(int)
            for f in files:
                basename = f.filepath.split("/")[-1].split(".")[0]
                dep_counts[basename] = session.query(DependencyRecord).filter(DependencyRecord.module_name.like(f"%{basename}%")).count()
            
            for f in files:
                inc = in_degrees.get(f.filepath, 0)
                outc = out_degrees.get(f.filepath, 0)
                symc = len(f.symbols)
                basename = f.filepath.split("/")[-1].split(".")[0]
                depc = dep_counts.get(basename, 0)
                
                score = (inc * 3) + (outc * 1) + (symc * 2) + (depc * 4)
                scores.append({
                    "filepath": f.filepath,
                    "score": score,
                    "in_degree": inc,
                    "out_degree": outc,
                    "symbol_count": symc
                })
            
            return sorted(scores, key=lambda x: x["score"], reverse=True)

    def get_file_detail(self, filepath: str) -> Dict:
        with self.SessionLocal() as session:
            f = session.query(FileRecord).filter(FileRecord.filepath == filepath).first()
            if not f:
                return {}
                
            fqns = [s.fully_qualified_name for s in f.symbols if s.fully_qualified_name]
            refs_in = []
            refs_out = []
            if fqns:
                refs_in_recs = session.query(ReferenceRecord).filter(ReferenceRecord.callee_fqn.in_(fqns)).all()
                for r in refs_in_recs:
                    refs_in.append({"caller": r.caller_fqn, "callee": r.callee_fqn, "kind": r.kind})
                    
                refs_out_recs = session.query(ReferenceRecord).filter(ReferenceRecord.caller_fqn.in_(fqns)).all()
                for r in refs_out_recs:
                    refs_out.append({"caller": r.caller_fqn, "callee": r.callee_fqn, "kind": r.kind})
                    
            return {
                "filepath": f.filepath,
                "language": f.language,
                "symbols": [{"name": s.name, "type": s.type, "docstring": s.docstring} for s in f.symbols],
                "deps": [{"module": d.module_name} for d in f.dependencies],
                "refs_in": refs_in,
                "refs_out": refs_out
            }

    def get_module_structure(self) -> List[Dict]:
        with self.SessionLocal() as session:
            files = session.query(FileRecord).all()
            modules = defaultdict(lambda: {"files": [], "total_symbols": 0, "total_deps": 0, "languages": set()})
            
            for f in files:
                parts = f.filepath.lstrip("./").split("/")
                module_path = "root" if len(parts) == 1 else "/".join(parts[:-1])
                
                modules[module_path]["files"].append(f.filepath)
                modules[module_path]["total_symbols"] += len(f.symbols)
                modules[module_path]["total_deps"] += len(f.dependencies)
                modules[module_path]["languages"].add(f.language)
                
            result = []
            for m_path, m_data in modules.items():
                result.append({
                    "module_path": m_path,
                    "files": m_data["files"],
                    "total_symbols": m_data["total_symbols"],
                    "total_deps": m_data["total_deps"],
                    "languages": list(m_data["languages"])
                })
            return result

    def get_entry_points(self) -> List[Dict]:
        with self.SessionLocal() as session:
            entry_points = []
            # Method 1: Common naming patterns
            patterns = ['%main%', '%cli%', '%app%', '%setup%', '%configure%', '%register%', '%create_app%', '%routes%']
            for p in patterns:
                recs = session.query(SymbolRecord, FileRecord).join(FileRecord).filter(SymbolRecord.name.like(p)).all()
                for s, f in recs:
                    entry_points.append({"fqn": s.fully_qualified_name, "file": f.filepath, "type": s.type, "reason": "Naming pattern match"})
                    
            # Method 2: Structural (0 incoming, >0 outgoing calls)
            # Fetch all fqns that make calls
            calling_fqns = session.query(ReferenceRecord.caller_fqn).filter(ReferenceRecord.kind == "Call").distinct().all()
            calling_fqns = {c[0] for c in calling_fqns if c[0]}
            
            # Fetch all fqns that are called
            called_fqns = session.query(ReferenceRecord.callee_fqn).filter(ReferenceRecord.kind == "Call").distinct().all()
            called_fqns = {c[0] for c in called_fqns if c[0]}
            
            # Entry points are those that call others but are never called
            structural_entry_fqns = calling_fqns - called_fqns
            if structural_entry_fqns:
                # Limit to prevent explosion
                structural_entry_fqns = list(structural_entry_fqns)[:20]
                recs = session.query(SymbolRecord, FileRecord).join(FileRecord).filter(SymbolRecord.fully_qualified_name.in_(structural_entry_fqns)).all()
                for s, f in recs:
                    entry_points.append({"fqn": s.fully_qualified_name, "file": f.filepath, "type": s.type, "reason": "Structural (calls others, never called)"})
                    
            # Deduplicate
            seen = set()
            unique_ep = []
            for ep in entry_points:
                if ep["fqn"] and ep["fqn"] not in seen:
                    seen.add(ep["fqn"])
                    unique_ep.append(ep)
                    
            return unique_ep

    def get_dependency_clusters(self) -> List[Dict]:
        # Simplified clustering based on directory prefix
        modules = self.get_module_structure()
        for m in modules:
            m["cluster_id"] = m["module_path"]
            m["internal_edges"] = 0
            m["external_deps"] = 0
        return modules

    def get_cross_module_edges(self) -> List[Dict]:
        with self.SessionLocal() as session:
            # Map file to module
            file_to_mod = {}
            for f in session.query(FileRecord).all():
                parts = f.filepath.lstrip("./").split("/")
                file_to_mod[f.filepath] = "root" if len(parts) == 1 else "/".join(parts[:-1])
                
            edges = defaultdict(int)
            for d, f in session.query(DependencyRecord, FileRecord).join(FileRecord).all():
                src_mod = file_to_mod.get(f.filepath, "unknown")
                # Very simple target module inference from dependency name
                target_mod_name = d.module_name.split(".")[0]
                edges[(src_mod, target_mod_name)] += 1
                
            result = []
            for (src, tgt), count in edges.items():
                if src != tgt:
                    result.append({"source_module": src, "target_module": tgt, "edge_count": count, "edge_types": ["import"]})
            return result

    def get_class_hierarchy_full(self) -> List[Dict]:
        with self.SessionLocal() as session:
            stmt = select(ReferenceRecord, FileRecord).join(FileRecord).where(ReferenceRecord.kind == "Inheritance")
            results = session.execute(stmt).all()
            return [{"child": r.caller_fqn, "parent": r.callee_fqn, "child_file": f.filepath, "parent_file": "unknown", "child_methods": [], "parent_methods": []} for r, f in results]

    def get_domain_entities(self) -> List[Dict]:
        with self.SessionLocal() as session:
            classes = session.query(SymbolRecord, FileRecord).join(FileRecord).filter(SymbolRecord.type == "class").all()
            entities = []
            
            fqn_to_refcount = defaultdict(int)
            for r in session.query(ReferenceRecord).all():
                fqn_to_refcount[r.callee_fqn] += 1
                
            for c, f in classes:
                if any(x in c.name for x in ["Mixin", "Base", "Abstract", "Meta", "Exception", "Error", "Test"]):
                    continue
                
                # Count methods roughly (this is simplified)
                method_count = session.query(SymbolRecord).filter(SymbolRecord.file_id == c.file_id, SymbolRecord.type.in_(["method", "function"])).count()
                
                if method_count >= 1 or fqn_to_refcount[c.fully_qualified_name] >= 1:
                    entities.append({
                        "name": c.name,
                        "fqn": c.fully_qualified_name,
                        "file": f.filepath,
                        "method_count": method_count,
                        "ref_count": fqn_to_refcount[c.fully_qualified_name],
                        "inherits_from": [],
                        "docstring": c.docstring
                    })
                    
            entities.sort(key=lambda x: (x["method_count"] * 2 + x["ref_count"]), reverse=True)
            return entities[:20]

    def get_callee_chains(self, start_fqn: str, max_depth: int = 5) -> List[Dict]:
        with self.SessionLocal() as session:
            chains = []
            current_wave = {start_fqn}
            seen = {start_fqn}
            
            for depth in range(max_depth):
                if not current_wave:
                    break
                next_wave = set()
                
                for fqn in current_wave:
                    refs = session.query(ReferenceRecord, FileRecord).join(FileRecord).filter(
                        ReferenceRecord.caller_fqn == fqn,
                        ReferenceRecord.kind == "Call"
                    ).all()
                    
                    for r, f in refs:
                        chains.append({"level": depth, "caller": r.caller_fqn, "callee": r.callee_fqn, "file": f.filepath})
                        if r.callee_fqn and r.callee_fqn not in seen:
                            seen.add(r.callee_fqn)
                            next_wave.add(r.callee_fqn)
                current_wave = next_wave
            return chains

    def get_most_referenced_symbols(self, limit: int = 50) -> List[Dict]:
        with self.SessionLocal() as session:
            counts = defaultdict(int)
            out_counts = defaultdict(int)
            for r in session.query(ReferenceRecord).all():
                if r.callee_fqn: counts[r.callee_fqn] += 1
                if r.caller_fqn: out_counts[r.caller_fqn] += 1
                
            top_fqns = sorted(counts.keys(), key=lambda k: counts[k], reverse=True)[:limit]
            
            result = []
            if top_fqns:
                symbols = session.query(SymbolRecord, FileRecord).join(FileRecord).filter(SymbolRecord.fully_qualified_name.in_(top_fqns)).all()
                for s, f in symbols:
                    result.append({
                        "fqn": s.fully_qualified_name,
                        "name": s.name,
                        "type": s.type,
                        "file": f.filepath,
                        "incoming_refs": counts.get(s.fully_qualified_name, 0),
                        "outgoing_refs": out_counts.get(s.fully_qualified_name, 0),
                        "docstring": s.docstring
                    })
            # Sort again because DB query might not preserve order
            result.sort(key=lambda x: x["incoming_refs"], reverse=True)
            return result
