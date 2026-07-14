def list_to_english(items: list, conjunction: str = "and") -> str:
    """Converts ['a', 'b', 'c'] to 'a, b, and c'."""
    if not items:
        return ""
    if len(items) == 1:
        return str(items[0])
    if len(items) == 2:
        return f"{items[0]} {conjunction} {items[1]}"
    return f"{', '.join(str(x) for x in items[:-1])}, {conjunction} {items[-1]}"

def clean_docstring(docstring: str) -> str:
    """Cleans up raw docstrings for prose integration."""
    if not docstring:
        return ""
    lines = [line.strip() for line in docstring.split('\n') if line.strip()]
    if not lines:
        return ""
    
    # Just take the first sentence/line for summaries
    first_line = lines[0]
    if first_line.startswith('"""') or first_line.startswith("'''"):
        first_line = first_line[3:].strip()
    return first_line.rstrip('.') + "."
