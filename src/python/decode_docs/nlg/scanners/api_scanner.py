import os
from python.decode_db.query_api import DBQueryAPI
import re

def scan_api_routes(api: DBQueryAPI) -> list:
    """Scan for API route registrations using both DB references and raw source parsing for decorators."""
    routes = []
    
    # 1. Regex scanning for Python decorators (since C++ parser currently skips them)
    # Match: @app.get('/path') or @router.post("/api")
    python_decorator_regex = re.compile(r'@(\w+)\.(get|post|put|delete|patch|route)\((?:["\']([^"\']+)["\'])?')
    
    # 2. Heuristics for JS/Express via the DB call graph
    js_objects = {"app", "router", "express", "server"}
    js_methods = {"get", "post", "put", "delete", "patch", "use"}

    all_files = api.get_all_files()
    all_refs = api.get_all_references()
    all_symbols = api.get_all_symbols()

    # Build lookups
    fqn_to_symbol = {}
    for s in all_symbols:
        fqn = s.get("fqn") or s.get("fully_qualified_name")
        if fqn:
            fqn_to_symbol[fqn] = s

    # --- Strategy A: Raw File Parsing for Python Decorators ---
    for f in all_files:
        filepath = f["filepath"]
        if not filepath.endswith(".py") or not os.path.exists(filepath):
            continue
            
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                
            for i, line in enumerate(lines):
                match = python_decorator_regex.search(line)
                if match:
                    obj_name, method, path = match.groups()
                    path = path or "/"
                    
                    # Look ahead to find the function name
                    handler_name = "unknown"
                    description = ""
                    for j in range(i + 1, min(i + 5, len(lines))):
                        func_match = re.search(r'def\s+([a-zA-Z0-9_]+)', lines[j])
                        if func_match:
                            handler_name = func_match.group(1)
                            # Try to find it in the DB to get docstring
                            for s in all_symbols:
                                if s["name"] == handler_name and s["file"] == filepath:
                                    description = s.get("docstring", "")
                                    break
                            break
                    
                    routes.append({
                        "method": method.upper() if method.upper() != "ROUTE" else "ALL",
                        "path": path,
                        "handler_fqn": f"{obj_name}.{handler_name}",
                        "handler_name": handler_name,
                        "file": os.path.basename(filepath),
                        "line": i + 1,
                        "description": description
                    })
        except Exception:
            pass

    # --- Strategy B: Call Graph for JS/Express ---
    for ref in all_refs:
        callee = ref.get("callee_fqn", "") or ref.get("callee", "")
        caller = ref.get("caller_fqn", "") or ref.get("caller", "")
        
        if not callee or not caller:
            continue

        parts = callee.rsplit(".", 1)
        if len(parts) == 2:
            obj_name, method_name = parts
            method_lower = method_name.lower()
            obj_base = obj_name.rsplit(".", 1)[-1].lower()

            if method_lower in js_methods and obj_base in js_objects:
                # Ensure the file is JS/TS
                filename = ref.get("file", "")
                if not filename.endswith((".js", ".ts", ".jsx", ".tsx")):
                    continue
                    
                # Try to get docstring
                handler_doc = fqn_to_symbol.get(caller, {}).get("docstring", "")

                routes.append({
                    "method": method_lower.upper(),
                    "path": "/...", # Dynamic paths are hard to extract from AST references alone
                    "handler_fqn": caller,
                    "handler_name": caller.rsplit(".", 1)[-1],
                    "file": filename,
                    "line": ref.get("line", 0),
                    "description": handler_doc,
                })

    # Deduplicate and sort
    seen = set()
    unique = []
    for r in routes:
        key = (r["method"], r["handler_name"], r["file"])
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return sorted(unique, key=lambda r: (r["file"], r["line"]))
