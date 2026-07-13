import os
import json
from datetime import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from python.decode_db.schema import FileRecord, SymbolRecord, DependencyRecord, ReferenceRecord

def _sanitize_path(filepath: str) -> str:
    """Convert a filepath to a safe JSON filename."""
    # Strip leading ./ or /
    path = filepath.lstrip("./")
    return path.replace("/", "_").replace("\\", "_") + ".json"

def _build_project_stats(session) -> dict:
    stats = {}
    stats["Total Files"] = session.query(FileRecord).count()
    
    # Python Files
    stats["Python Files"] = session.query(FileRecord).where(func.lower(FileRecord.language) == "python").count()
    # C++ Files
    stats["C++ Files"] = session.query(FileRecord).where(
        (func.lower(FileRecord.language) == "c++") | (func.lower(FileRecord.language) == "cpp")
    ).count()
    
    stats["Total Classes"] = session.query(SymbolRecord).where(func.lower(SymbolRecord.type) == "class").count()
    stats["Total Functions"] = session.query(SymbolRecord).where(
        (func.lower(SymbolRecord.type) == "function") | (func.lower(SymbolRecord.type) == "method")
    ).count()
    stats["Total References"] = session.query(ReferenceRecord).count()
    
    return stats

def _build_module_index(session) -> list:
    # A module index with module name, language, number of symbols
    modules = []
    files = session.query(FileRecord).all()
    for f in files:
        sym_count = session.query(SymbolRecord).where(SymbolRecord.file_id == f.id).count()
        if sym_count > 0:
            modules.append({
                "module": f.filepath,
                "language": f.language,
                "symbols": sym_count
            })
    return modules

def _build_per_file_context(session, file_record: FileRecord) -> dict:
    context = {
        "filepath": file_record.filepath,
        "language": file_record.language,
        "symbols": [],
        "imports": [],
        "calls": []
    }
    
    for sym in file_record.symbols:
        context["symbols"].append({
            "name": sym.name,
            "fqn": sym.fully_qualified_name,
            "kind": sym.type,
            "signature": sym.signature,
            "return_type": sym.return_type,
            "docstring": sym.docstring,
            "lines": [sym.start_line, sym.end_line]
        })
        
    for dep in file_record.dependencies:
        context["imports"].append(dep.module_name)
    context["imports"] = list(set(context["imports"]))
        
    for ref in file_record.references:
        context["calls"].append({
            "from": ref.caller_fqn,
            "to": ref.callee_fqn,
            "kind": ref.kind,
            "line": ref.line_number
        })
        
    return context

def _write_snapshot_md(stats: dict, modules: list, output_dir: str):
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    
    lines = [
        "# DECODE Project Snapshot",
        f"Generated: {timestamp} | Files: {stats['Total Files']} | Symbols: {stats['Total Classes'] + stats['Total Functions']} | References: {stats['Total References']}",
        "",
        "## Project Statistics",
        "| Metric | Count |",
        "|--------|-------|"
    ]
    
    for k, v in stats.items():
        lines.append(f"| {k} | {v} |")
        
    lines.extend([
        "",
        "## Module Index",
        "| Module | Language | Symbols |",
        "|--------|----------|---------|"
    ])
    
    # Sort modules by filepath
    modules.sort(key=lambda x: x["module"])
    for m in modules:
        lines.append(f"| {m['module']} | {m['language']} | {m['symbols']} |")
        
    lines.extend([
        "",
        "## Key Entry Points",
        "- `scripts/run_indexer.py::run_indexer()` — Main indexer entry point",
        "- `decode.py::main()` — CLI router",
        "",
        "## How to Read This Project",
        "See `context/` directory for per-file details."
    ])
    
    with open(os.path.join(output_dir, "SNAPSHOT.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def _write_context_json(file_data: dict, output_dir: str):
    filename = _sanitize_path(file_data["filepath"])
    out_path = os.path.join(output_dir, "context", filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(file_data, f, indent=2)

def generate_snapshot(db_path: str = "decode_graph.db", project_root: str = ".", output_dir: str = ".decode"):
    print(f"📸 Generating DECODE snapshot from {db_path}...")
    
    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    
    context_dir = os.path.join(output_dir, "context")
    os.makedirs(context_dir, exist_ok=True)
    
    with Session() as session:
        stats = _build_project_stats(session)
        modules = _build_module_index(session)
        
        _write_snapshot_md(stats, modules, output_dir)
        
        files = session.query(FileRecord).all()
        for f in files:
            file_data = _build_per_file_context(session, f)
            _write_context_json(file_data, output_dir)
            
    print(f"✅ Snapshot successfully saved to {output_dir}/")
