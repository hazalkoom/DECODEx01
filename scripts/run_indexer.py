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
    stale_filepaths = []
    
    skipped_count = 0

    # We need a safe starting ID for our manual ID generation to avoid primary key collisions
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
                continue # Skip! It hasn't changed since last scan.
            else:
                # The file changed. Mark it for deletion so we can insert the fresh data.
                stale_filepaths.append(path)

        lang = codelens_core.detect_language(path)
        
        files_to_insert.append({
            "id": file_id_counter,
            "filepath": path,
            "language": lang,
            "last_modified": mtime # Save the timestamp!
        })
        
        if parser.set_language(lang.lower()):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    source_code = f.read()
                    
                symbols = parser.extract_symbols(source_code)
                for sym in symbols:
                    symbols_data.append({
                        "file_id": file_id_counter,
                        "name": sym.name,
                        "type": sym.type,
                        "start_line": sym.start_line,
                        "end_line": sym.end_line
                    })
                    
                deps = parser.extract_dependencies(source_code)
                for dep in deps:
                    deps_data.append({
                        "file_id": file_id_counter,
                        "module_name": dep.module_name,
                        "imported_name": getattr(dep, 'imported_name', None), 
                        "line_number": dep.line_number
                    })
            except Exception:
                pass
                
        file_id_counter += 1

    # 3. Clean up stale data before inserting the new data
    if stale_filepaths:
        print(f"♻️  Updating {len(stale_filepaths)} modified files...")
        db.remove_stale_files(stale_filepaths)

    # 4. Insert only the fresh data
    if files_to_insert:
        print(f"💾 Saving {len(files_to_insert)} new/updated files to the database...")
        db.ingest_project_data(files_to_insert, symbols_data, deps_data)
    else:
        print("✅ No new changes detected.")
    
    end_time = time.time()
    print(f"⏭️  Skipped {skipped_count} unchanged files.")
    print(f"🏁 Smart Indexing complete in {end_time - start_time:.3f} seconds!")

if __name__ == "__main__":
    run_indexer(".")