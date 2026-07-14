import json
import os
from python.decode_db.query_api import DBQueryAPI

DEFAULT_SCHEMA = {
    "sections": [
        {
            "title": "Response Conventions",
            "trigger": {"symbol_pattern": "Response|JsonResponse|HTTPResponse"},
            "template": "All API endpoints in this project return responses using the `{matched_class}` class defined in `{matched_file}`. This ensures a consistent response format across the application."
        },
        {
            "title": "Authentication",
            "trigger": {"symbol_pattern": "Auth|Token|JWT|Session|Login|Middleware"},
            "template": "Authentication is handled by the `{matched_class}` component in `{matched_file}`. Requests must include valid credentials before accessing protected endpoints."
        },
        {
            "title": "User Roles",
            "trigger": {"symbol_pattern": "Admin|Owner|Moderator|Role|Permission"},
            "template": "The system defines the following user roles: {matched_names}. These are managed by `{matched_class}` in `{matched_file}`."
        },
        {
            "title": "Database Access",
            "trigger": {"symbol_pattern": "Database|Repository|Session|Connection|Pool"},
            "template": "Database operations are centralized through `{matched_class}` in `{matched_file}`. This component manages connection pooling and query execution."
        },
        {
            "title": "Error Handling",
            "trigger": {"symbol_pattern": "Error|Exception|Handler|Middleware"},
            "template": "Errors are managed by `{matched_class}` in `{matched_file}`. The application uses structured error responses to communicate failures."
        },
    ]
}

def load_schema(project_root: str) -> dict:
    """Load a reference_template.json or fall back to defaults."""
    custom_path = os.path.join(project_root, ".decode", "reference_template.json")
    if os.path.exists(custom_path):
        try:
            with open(custom_path) as f:
                return json.load(f)
        except Exception:
            pass
    return DEFAULT_SCHEMA

def populate_sections(schema: dict, api: DBQueryAPI) -> list:
    """Match AST symbols against schema triggers using strict scoring (Classes only, file paths)."""
    import re
    all_symbols = api.get_all_symbols()
    populated = []

    for section in schema.get("sections", []):
        trigger = section.get("trigger", {})
        pattern = trigger.get("symbol_pattern", "")
        if not pattern:
            continue

        regex = re.compile(pattern, re.IGNORECASE)
        scored_matches = []
        
        for sym in all_symbols:
            # Stricter heuristic 1: Only match Classes (or Types), not functions/variables
            # Exception: if it's explicitly a middleware, it might be a function
            is_class = sym.get("type", "").lower() in ["class", "struct", "interface", "type"]
            is_middleware = "middleware" in pattern.lower() and sym.get("type", "").lower() == "function"
            
            if not (is_class or is_middleware):
                continue
                
            score = 0
            # Score from name
            if regex.search(sym.get("name", "")):
                score += 2
                
            # Score from file path context
            filepath = sym.get("file", "").lower()
            if regex.search(filepath):
                score += 1
                
            if score >= 2: # Require a strong match
                scored_matches.append((score, sym))

        if scored_matches:
            # Sort by score descending
            scored_matches.sort(key=lambda x: x[0], reverse=True)
            matched = [m[1] for m in scored_matches]
            
            # Use the best match for the template, collect all names
            first = matched[0]
            all_names = list(set(m["name"] for m in matched))

            prose = section["template"].format(
                matched_class=first.get("name", "unknown"),
                matched_file=first.get("file", "unknown").split("/")[-1],
                matched_names=", ".join(f"`{n}`" for n in all_names[:5]),
            )

            populated.append({
                "title": section["title"],
                "prose": prose,
                "matches": len(matched),
            })

    return populated
