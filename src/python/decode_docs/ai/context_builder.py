"""
context_builder.py

Extracts the minimum necessary data from the SQLite DB to build
focused, token-efficient prompts. Never dumps the whole XML.
Each method returns a compact string "brief" for a specific doc type.
"""
import os
from python.decode_db.query_api import DBQueryAPI


def _fmt_symbols(symbols: list, max_n: int = 25) -> str:
    """Render a compact symbol list for prompt injection."""
    lines = []
    for s in symbols[:max_n]:
        sig = s.get("signature") or s.get("name", "")
        doc = (s.get("docstring") or "").strip().split("\n")[0][:80]
        kind = s.get("type", "?")
        line = f"  [{kind}] {sig}"
        if doc:
            line += f" — {doc}"
        lines.append(line)
    return "\n".join(lines) if lines else "  (no symbols found)"


def _fmt_files(files: list, max_n: int = 30) -> str:
    lines = []
    for f in files[:max_n]:
        fp = f.get("filepath") or f.get("file", "")
        lang = f.get("language", "")
        lines.append(f"  {fp}  [{lang}]")
    return "\n".join(lines) if lines else "  (no files)"


def _fmt_deps(deps: list, max_n: int = 20) -> str:
    names = sorted(set(d.get("module_name", "") for d in deps))[:max_n]
    return "\n".join(f"  - {n}" for n in names) if names else "  (none)"


def build_overview_brief(api: DBQueryAPI) -> str:
    """Brief for the README/Project Overview document."""
    files = api.get_all_files()
    symbols = api.get_all_symbols()
    langs = {}
    for f in files:
        l = f.get("language", "Unknown")
        langs[l] = langs.get(l, 0) + 1

    lang_str = ", ".join(f"{l} ({c} files)" for l, c in sorted(langs.items(), key=lambda x: -x[1])[:6])
    total_files = len(files)
    total_syms = len(symbols)

    classes = [s for s in symbols if s.get("type", "").lower() == "class"]
    funcs = [s for s in symbols if s.get("type", "").lower() in ("function", "method")]

    # Entry-point candidates: files with many incoming references
    entry_files = [f for f in files if any(
        kw in (f.get("filepath") or "") for kw in ["main", "cli", "app", "server", "index", "entry", "decode.py", "run_"]
    )][:5]

    brief = f"""PROJECT STATS:
  Total files: {total_files}
  Languages: {lang_str}
  Total symbols: {total_syms} ({len(classes)} classes, {len(funcs)} functions/methods)

LIKELY ENTRY POINTS:
{_fmt_files(entry_files)}

MOST IMPORTANT CLASSES:
{_fmt_symbols(classes[:15])}
"""
    return brief


def build_architecture_brief(api: DBQueryAPI) -> str:
    """Brief for the Architecture document."""
    files = api.get_all_files()

    # Group files by top-level directory
    folders: dict = {}
    for f in files:
        fp = f.get("filepath") or ""
        parts = fp.lstrip("./").split("/")
        top = parts[0] if parts else "root"
        folders.setdefault(top, []).append(fp)

    folder_str = ""
    for folder, fps in sorted(folders.items(), key=lambda x: -len(x[1]))[:10]:
        folder_str += f"  {folder}/  ({len(fps)} files)\n"

    classes = [s for s in api.get_all_symbols() if s.get("type", "").lower() == "class"]
    return f"""TOP-LEVEL DIRECTORIES:
{folder_str}
KEY CLASSES (the backbone of the architecture):
{_fmt_symbols(classes[:20])}
"""


def build_module_brief(api: DBQueryAPI) -> str:
    """Brief for the Module Guide — all files with their symbols."""
    files = api.get_all_files()
    symbols = api.get_all_symbols()

    # Map file path -> symbols
    by_file: dict = {}
    for s in symbols:
        fp = s.get("file", "")
        by_file.setdefault(fp, []).append(s)

    lines = []
    for f in sorted(files, key=lambda x: x.get("filepath", ""))[:40]:
        fp = f.get("filepath", "")
        syms = by_file.get(fp, [])
        sym_names = ", ".join(s.get("name", "") for s in syms[:6])
        lines.append(f"  {fp}  →  {sym_names or '(no symbols)'}")

    return "FILE → SYMBOLS MAP:\n" + "\n".join(lines)


def build_contributing_brief(api: DBQueryAPI, project_root: str = ".") -> str:
    """Brief for the Contributing / Setup guide — scans root config files."""
    config_files = []
    targets = [
        "package.json", "requirements.txt", "pyproject.toml",
        "CMakeLists.txt", "Makefile", "docker-compose.yml",
        "Dockerfile", "setup.py", "setup.cfg", "go.mod", "Cargo.toml",
        ".github/CONTRIBUTING.md", "CONTRIBUTING.md", "README.md"
    ]
    snippets = []
    for target in targets:
        full = os.path.join(project_root, target)
        if os.path.isfile(full):
            config_files.append(target)
            try:
                with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                    content = fh.read(600)  # first 600 chars only
                snippets.append(f"--- {target} (first 600 chars) ---\n{content}\n")
            except Exception:
                pass

    detected = "\n".join(f"  - {c}" for c in config_files)
    snippet_str = "\n".join(snippets[:4])  # max 4 files to keep tokens low
    return f"DETECTED CONFIG FILES:\n{detected}\n\nCONFIG SNIPPETS:\n{snippet_str}"


def build_api_brief(api: DBQueryAPI) -> str:
    """Brief for the API Reference — all public functions with signatures."""
    symbols = api.get_all_symbols()
    public_funcs = [
        s for s in symbols
        if s.get("type", "").lower() in ("function", "method")
        and not (s.get("name") or "").startswith("_")
    ]

    lines = []
    for s in public_funcs[:50]:
        sig = s.get("signature") or s.get("name", "")
        doc = (s.get("docstring") or "").strip().split("\n")[0][:100]
        file_ = (s.get("file") or "").split("/")[-1]
        ret = s.get("return_type") or ""
        line = f"  {file_}: {sig}"
        if ret:
            line += f" -> {ret}"
        if doc:
            line += f"\n    \"{doc}\""
        lines.append(line)

    return "PUBLIC FUNCTIONS & METHODS:\n" + "\n".join(lines)


def build_glossary_brief(api: DBQueryAPI) -> str:
    """Brief for Glossary — all class names and unique module names."""
    symbols = api.get_all_symbols()
    classes = [s for s in symbols if s.get("type", "").lower() == "class"]
    deps = api.get_all_dependencies() if hasattr(api, "get_all_dependencies") else []
    mod_names = sorted(set(d.get("module_name", "").split(".")[0] for d in deps if d.get("module_name")))[:20]

    class_lines = _fmt_symbols(classes[:30])
    mod_str = "\n".join(f"  - {m}" for m in mod_names)
    return f"CLASSES (define the glossary terms):\n{class_lines}\n\nKEY MODULES IMPORTED:\n{mod_str}"


def build_callflow_brief(api: DBQueryAPI) -> str:
    """Brief for Story of a Request — top call chains."""
    symbols = api.get_all_symbols()
    refs = api.get_all_references() if hasattr(api, "get_all_references") else []

    # Find most-called functions (highest in-degree)
    call_counts: dict = {}
    for r in refs:
        callee = r.get("callee_fqn") or r.get("callee", "")
        if callee:
            call_counts[callee] = call_counts.get(callee, 0) + 1

    top_callees = sorted(call_counts.items(), key=lambda x: -x[1])[:15]
    top_str = "\n".join(f"  {fqn}  (called {cnt}x)" for fqn, cnt in top_callees)

    # Most-called callers (highest out-degree)
    caller_counts: dict = {}
    for r in refs:
        caller = r.get("caller_fqn") or r.get("caller", "")
        if caller:
            caller_counts[caller] = caller_counts.get(caller, 0) + 1

    top_callers = sorted(caller_counts.items(), key=lambda x: -x[1])[:10]
    caller_str = "\n".join(f"  {fqn}  (calls {cnt} things)" for fqn, cnt in top_callers)

    return f"MOST-CALLED FUNCTIONS (hot paths):\n{top_str}\n\nBIGGEST ORCHESTRATORS (call the most):\n{caller_str}"
