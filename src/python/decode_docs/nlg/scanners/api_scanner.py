from python.decode_db.query_api import DBQueryAPI
import re

# Patterns that indicate HTTP route registration
ROUTE_PATTERNS = {
    # Python: Flask/FastAPI/Django
    "python": {
        "decorators": ["get", "post", "put", "delete", "patch", "route", "api_view"],
        "objects": ["app", "router", "blueprint", "api", "urlpatterns"],
    },
    # JavaScript: Express
    "javascript": {
        "decorators": ["get", "post", "put", "delete", "patch", "use"],
        "objects": ["app", "router", "express", "server"],
    },
}

def scan_api_routes(api: DBQueryAPI) -> list:
    """Scan the call graph DB for API route registrations."""
    routes = []
    all_refs = api.get_all_references()
    all_symbols = api.get_all_symbols()

    # Build a lookup: fqn -> symbol info (for docstrings)
    fqn_to_symbol = {}
    for s in all_symbols:
        if s.get("fqn"):
            fqn_to_symbol[s["fqn"]] = s
        elif s.get("fully_qualified_name"):
            fqn_to_symbol[s["fully_qualified_name"]] = s

    for ref in all_refs:
        callee = ref.get("callee_fqn", "") or ref.get("callee", "")
        caller = ref.get("caller_fqn", "") or ref.get("caller", "")
        
        if not callee or not caller:
            continue

        # Check if callee looks like a route registration
        # e.g., callee = "app.get" or "router.post"
        parts = callee.rsplit(".", 1)
        if len(parts) == 2:
            obj_name, method_name = parts
            method_lower = method_name.lower()

            for lang, patterns in ROUTE_PATTERNS.items():
                if method_lower in patterns["decorators"]:
                    obj_base = obj_name.rsplit(".", 1)[-1].lower()
                    if obj_base in patterns["objects"]:
                        # Found a route registration!
                        http_method = method_lower.upper()
                        if http_method == "ROUTE":
                            http_method = "ALL"

                        # Try to get docstring from the handler function
                        handler_doc = ""
                        if caller in fqn_to_symbol:
                            handler_doc = fqn_to_symbol[caller].get("docstring", "") or ""

                        routes.append({
                            "method": http_method,
                            "handler_fqn": caller,
                            "handler_name": caller.rsplit(".", 1)[-1],
                            "file": ref.get("file", "unknown"),
                            "line": ref.get("line", 0),
                            "description": handler_doc,
                        })

    # Deduplicate
    seen = set()
    unique = []
    for r in routes:
        key = (r["method"], r["handler_fqn"])
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return sorted(unique, key=lambda r: (r["file"], r["line"]))
