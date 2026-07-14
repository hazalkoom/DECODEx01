"""
ai_docs_generator.py

Orchestrates AI-powered documentation generation.
Generates 6 high-quality documents using minimal tokens per call:
  1. README.md           — Project overview and quick start
  2. ARCHITECTURE.md     — System design and component map
  3. MODULE_GUIDE.md     — File-by-file guide for contributors
  4. CONTRIBUTING.md     — Setup, testing, and PR workflow
  5. API_REFERENCE.md    — All public functions documented
  6. GLOSSARY.md         — Plain-English dictionary of key terms
  7. STORY_OF_A_REQUEST.md — Request lifecycle walkthrough

Token-efficiency strategy:
- Each document gets its OWN targeted prompt from context_builder.py
- The prompt only carries the data relevant to THAT document
- The shared system prompt is small and reusable
- max_tokens is tuned per doc type
"""
import os

from python.decode_db.query_api import DBQueryAPI
from .context_builder import (
    build_overview_brief,
    build_architecture_brief,
    build_module_brief,
    build_contributing_brief,
    build_api_brief,
    build_glossary_brief,
    build_callflow_brief,
)
from .prompts import (
    SENIOR_ENGINEER_SYSTEM,
    prompt_readme,
    prompt_architecture,
    prompt_module_guide,
    prompt_contributing,
    prompt_api_reference,
    prompt_glossary,
    prompt_callflow,
)
from .llm_client import call_llm


# (filename, brief_builder, prompt_builder, max_tokens)
DOC_PLAN = [
    ("README.md",               build_overview_brief,      prompt_readme,        1800),
    ("ARCHITECTURE.md",         build_architecture_brief,  prompt_architecture,  1600),
    ("MODULE_GUIDE.md",         build_module_brief,        prompt_module_guide,  2000),
    ("CONTRIBUTING.md",         build_contributing_brief,  prompt_contributing,  1400),
    ("API_REFERENCE.md",        build_api_brief,           prompt_api_reference, 2200),
    ("GLOSSARY.md",             build_glossary_brief,      prompt_glossary,      1400),
    ("STORY_OF_A_REQUEST.md",   build_callflow_brief,      prompt_callflow,      1600),
]


def _detect_project_name(project_root: str, api: DBQueryAPI) -> str:
    """Try to detect a real project name from pyproject.toml, package.json, or CMakeLists."""
    # pyproject.toml
    for candidate in ["pyproject.toml", "package.json", "Cargo.toml", "CMakeLists.txt"]:
        path = os.path.join(project_root, candidate)
        if os.path.isfile(path):
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read(800)
                # pyproject.toml: name = "..."
                import re
                m = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
                if m:
                    return m.group(1)
            except Exception:
                pass
    # Fallback: use root folder name
    return os.path.basename(os.path.abspath(project_root))


def generate_ai_docs(db_path: str, project_root: str, output_dir: str):
    """
    Main entry point. Generates all AI docs into output_dir.
    """
    print(f"🤖 AI Doc Generator starting — reading from {db_path}")
    print(f"   Provider: {os.environ.get('DECODE_AI_PROVIDER', 'openai')}")
    print(f"   Model: {os.environ.get('DECODE_AI_MODEL', 'gpt-4o-mini')}")
    print()

    api = DBQueryAPI(db_path)
    project_name = _detect_project_name(project_root, api)
    print(f"   Project detected: {project_name}")
    print()

    os.makedirs(output_dir, exist_ok=True)
    generated = []

    for i, (filename, brief_fn, prompt_fn, max_tokens) in enumerate(DOC_PLAN, 1):
        print(f"  [{i}/{len(DOC_PLAN)}] Generating {filename}...", end="", flush=True)
        try:
            # Build context-specific brief (small, targeted)
            if filename == "CONTRIBUTING.md":
                brief = brief_fn(api, project_root)
            else:
                brief = brief_fn(api)

            # Build user prompt
            user_prompt = prompt_fn(brief, project_name)

            # Call the LLM
            content = call_llm(
                system_prompt=SENIOR_ENGINEER_SYSTEM,
                user_prompt=user_prompt,
                max_tokens=max_tokens,
            )

            # Write output
            out_path = os.path.join(output_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content + "\n")

            print(f" ✅  ({len(content)} chars)")
            generated.append(filename)

        except Exception as e:
            print(f" ❌  Error: {e}")

    # Generate index
    _write_index(output_dir, project_name, generated)

    print()
    print(f"✅ Generated {len(generated)}/{len(DOC_PLAN)} AI docs in '{output_dir}/'")
    print()
    print("📖 Documents:")
    for f in generated:
        print(f"   docs/{f}")


def _write_index(output_dir: str, project_name: str, generated: list):
    """Write a simple index.md linking all generated docs."""
    lines = [
        f"# {project_name} — Documentation Index",
        "",
        "Generated by [DECODE](https://github.com/hazalkoom/DECODEx01) — AI-powered codebase intelligence.",
        "",
        "## Documents",
        "",
    ]
    descriptions = {
        "README.md":             "Project overview, features, and quick start",
        "ARCHITECTURE.md":       "System design, component map, and layer relationships",
        "MODULE_GUIDE.md":       "File-by-file guide for contributors",
        "CONTRIBUTING.md":       "Setup, testing, and pull request workflow",
        "API_REFERENCE.md":      "All public functions and their documentation",
        "GLOSSARY.md":           "Plain-English dictionary of key terms and classes",
        "STORY_OF_A_REQUEST.md": "Request lifecycle walkthrough through the codebase",
    }
    for filename in generated:
        desc = descriptions.get(filename, "")
        lines.append(f"- [{filename}](./{filename}) — {desc}")

    lines.extend(["", "---", "_Auto-generated. Do not edit manually._"])

    out_path = os.path.join(output_dir, "index.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
