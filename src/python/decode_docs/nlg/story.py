from python.decode_db.query_api import DBQueryAPI

def find_deepest_call_chain(api: DBQueryAPI) -> list:
    """Find the single longest execution path through the call graph (DFS)."""
    entry_points = api.get_entry_points()
    if not entry_points:
        return []

    best_chain = []

    for ep in entry_points[:5]:  # Limit to top 5 entry points
        chain = _dfs_longest(api, ep["fqn"], set(), [])
        if len(chain) > len(best_chain):
            best_chain = chain

    return best_chain

def _dfs_longest(api, current_fqn, visited, path):
    """DFS to find the longest chain from current_fqn."""
    if current_fqn in visited or len(path) > 15:
        return path
    visited.add(current_fqn)
    path = path + [current_fqn]

    calls = api.find_calls_by(current_fqn)
    if not calls:
        return path

    longest = path
    for call in calls[:5]:  # Limit branching
        callee = call.get("callee_fqn", "") or call.get("callee", "")
        if callee and callee not in visited:
            candidate = _dfs_longest(api, callee, visited.copy(), path)
            if len(candidate) > len(longest):
                longest = candidate

    return longest

def generate_story_prose(chain: list) -> str:
    """Convert a call chain into a narrative paragraph."""
    if not chain:
        return "No significant execution path was detected."

    steps = []
    for i, fqn in enumerate(chain):
        name = fqn.rsplit(".", 1)[-1]
        if i == 0:
            steps.append(f"Execution begins at `{name}`.")
        elif i == len(chain) - 1:
            steps.append(f"Finally, the result is handled by `{name}`.")
        else:
            verbs = ["delegates to", "passes control to", "invokes", "coordinates with", "hands off to"]
            verb = verbs[i % len(verbs)]
            steps.append(f"It then {verb} `{name}`.")

    return " ".join(steps)

def generate_story_mermaid(chain: list) -> str:
    """Generate a Mermaid sequence diagram from the chain."""
    if len(chain) < 2:
        return ""

    lines = ["sequenceDiagram"]
    for i in range(len(chain) - 1):
        caller = chain[i].rsplit(".", 1)[-1]
        callee = chain[i+1].rsplit(".", 1)[-1]
        # Sanitize for mermaid
        caller = caller.replace("<", "").replace(">", "").replace(" ", "_")
        callee = callee.replace("<", "").replace(">", "").replace(" ", "_")
        lines.append(f"    {caller}->>+{callee}: calls")
        if i == len(chain) - 2:
            lines.append(f"    {callee}-->>-{caller}: returns")

    return "\n".join(lines)
