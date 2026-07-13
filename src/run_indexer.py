import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import codelens_core
from python.decode_db.manager import DBManager

def run_indexer(target_directory: str, db_name: str = "decode_graph.db"):
    print(f"🚀 Starting Smart Indexer on: {target_directory}")
    start_time = time.time()
    
    parser = codelens_core.ASTParser()
    db = DBManager(db_name)
    
    # 1. Ask the DB what it already knows
    existing_files = db.get_existing_files()
    
    print("📂 Scanning directory for files...")
    filepaths = codelens_core.walk_repository(target_directory)
    
    files_to_insert = []
    symbols_data = []
    deps_data = []
    refs_data = [] # NEW: We need a list to hold the Call Graph data
    
    stale_filepaths = []
    skipped_count = 0

    file_id_counter = int(time.time() * 1000) 

    for path in filepaths:
        if not os.path.isfile(path):
            continue

        if "decode_graph.db" in path:
            continue
            
        mtime = os.path.getmtime(path)
        
        # 2. THE BRAIN: Check if we can skip this file
        if path in existing_files:
            if existing_files[path] >= mtime:
                skipped_count += 1
                continue 
            else:
                stale_filepaths.append(path)

        lang = codelens_core.detect_language(path)
        
        files_to_insert.append({
            "id": file_id_counter,
            "filepath": path,
            "language": lang,
            "last_modified": mtime
        })
        
        if parser.set_language(lang.lower()):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    source_code = f.read()
                    
                # THE MASSIVE UPGRADE: Single-Pass Parsing
                file_context = parser.analyze_file(path, source_code)
                
                for sym in file_context.symbols:
                    symbols_data.append({
                        "file_id": file_id_counter,
                        "name": sym.name,
                        "fully_qualified_name": sym.fully_qualified_name,
                        "signature": sym.signature,
                        "return_type": sym.return_type,
                        "type": sym.kind.name, # .name converts the Pybind11 Enum to a string (e.g., "Function")
                        "docstring": sym.docstring,
                        "start_line": sym.start_line,
                        "end_line": sym.end_line
                    })
                    
                for dep in file_context.dependencies:
                    deps_data.append({
                        "file_id": file_id_counter,
                        "module_name": dep.module_name,
                        "imported_name": getattr(dep, 'imported_name', None), 
                        "line_number": dep.line_number
                    })
                    
                # NEW: Extract the references for the Call Graph
                for ref in file_context.references:
                    refs_data.append({
                        "file_id": file_id_counter,
                        "caller_fqn": ref.caller_fqn,
                        "callee_fqn": ref.callee_fqn,
                        "kind": ref.kind.name, # Converts the Enum to a string (e.g., "Call")
                        "line_number": ref.line_number
                    })
                    
            except Exception as e:
                print(f"⚠️ Error parsing {path}: {e}")
                
        file_id_counter += 1

    if stale_filepaths:
        print(f"♻️  Updating {len(stale_filepaths)} modified files...")
        db.remove_stale_files(stale_filepaths)

    if files_to_insert:
        print(f"💾 Saving {len(files_to_insert)} new/updated files to the database...")
        # Note: We are passing refs_data to the DB manager now!
        db.ingest_project_data(files_to_insert, symbols_data, deps_data, refs_data)
    else:
        print("✅ No new changes detected.")
    
    end_time = time.time()
    print(f"⏭️  Skipped {skipped_count} unchanged files.")
    print(f"🏁 Smart Indexing complete in {end_time - start_time:.3f} seconds!")

if __name__ == "__main__":
    run_indexer(".")