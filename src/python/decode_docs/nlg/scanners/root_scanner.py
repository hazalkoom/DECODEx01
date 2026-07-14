import os
import json
import re

# The master knowledge base: maps detected files to human-readable setup instructions
CONFIG_KNOWLEDGE_BASE = {
    "package.json": {
        "tool": "npm",
        "prerequisite": "Node.js 18+ and npm 9+",
        "install_cmd": "npm install",
        "run_cmd": "npm start",
        "dev_cmd": "npm run dev",
    },
    "requirements.txt": {
        "tool": "pip",
        "prerequisite": "Python 3.10+",
        "install_cmd": "pip install -r requirements.txt",
    },
    "pyproject.toml": {
        "tool": "poetry",
        "prerequisite": "Python 3.10+ and Poetry 1.8+",
        "install_cmd": "poetry install",
        "run_cmd": "poetry run python main.py",
    },
    "Cargo.toml": {
        "tool": "cargo",
        "prerequisite": "Rust 1.70+ and Cargo",
        "install_cmd": "cargo build",
        "run_cmd": "cargo run",
    },
    "go.mod": {
        "tool": "go",
        "prerequisite": "Go 1.21+",
        "install_cmd": "go mod download",
        "run_cmd": "go run .",
    },
    "CMakeLists.txt": {
        "tool": "cmake",
        "prerequisite": "CMake 3.20+ and a C++ compiler (GCC 12+ or Clang 15+)",
        "install_cmd": "mkdir build && cd build && cmake .. && make",
    },
    "Makefile": {
        "tool": "make",
        "prerequisite": "GNU Make",
        "install_cmd": "make",
    },
    "docker-compose.yml": {
        "tool": "docker",
        "prerequisite": "Docker 24+ and Docker Compose V2",
        "install_cmd": "docker compose up -d",
        "section": "Running with Docker",
    },
    "Dockerfile": {
        "tool": "docker",
        "prerequisite": "Docker 24+",
        "install_cmd": "docker build -t app . && docker run app",
    },
}

def scan_project_root(project_root: str) -> dict:
    """Scan root directory for config files and extract setup metadata."""
    result = {
        "detected_configs": [],
        "prerequisites": [],
        "install_steps": [],
        "run_steps": [],
        "docker_section": None,
        "readme_summary": None,
        "project_name": os.path.basename(os.path.abspath(project_root)),
    }

    for filename, knowledge in CONFIG_KNOWLEDGE_BASE.items():
        filepath = os.path.join(project_root, filename)
        if os.path.exists(filepath):
            result["detected_configs"].append(filename)
            result["prerequisites"].append(knowledge["prerequisite"])
            result["install_steps"].append({
                "tool": knowledge["tool"],
                "command": knowledge["install_cmd"],
            })
            if "run_cmd" in knowledge:
                result["run_steps"].append(knowledge["run_cmd"])
            if knowledge.get("section") == "Running with Docker":
                result["docker_section"] = knowledge

    # Extract README first line as project description
    for readme_name in ["README.md", "readme.md", "README.rst", "README"]:
        readme_path = os.path.join(project_root, readme_name)
        if os.path.exists(readme_path):
            with open(readme_path, "r", errors="ignore") as f:
                lines = [l.strip() for l in f.readlines()[:10] if l.strip()]
                # Skip markdown headers to find the first descriptive line
                for line in lines:
                    if not line.startswith("#") and len(line) > 20:
                        result["readme_summary"] = line
                        break
            break

    # Extract project name from package.json if available
    pkg_json = os.path.join(project_root, "package.json")
    if os.path.exists(pkg_json):
        try:
            with open(pkg_json) as f:
                pkg = json.load(f)
                result["project_name"] = pkg.get("name", result["project_name"])
                if not result["readme_summary"]:
                    result["readme_summary"] = pkg.get("description", "")
        except: pass

    # Extract from pyproject.toml
    pyproject = os.path.join(project_root, "pyproject.toml")
    if os.path.exists(pyproject):
        try:
            with open(pyproject) as f:
                content = f.read()
                name_match = re.search(r'name\s*=\s*"([^"]+)"', content)
                desc_match = re.search(r'description\s*=\s*"([^"]+)"', content)
                if name_match:
                    result["project_name"] = name_match.group(1)
                if desc_match and not result["readme_summary"]:
                    result["readme_summary"] = desc_match.group(1)
        except: pass

    return result
