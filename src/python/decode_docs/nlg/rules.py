from .analyzer import determine_file_role
from .formatter import list_to_english, clean_docstring
from .templates import *

def generate_project_overview_prose(data: dict) -> str:
    languages = list(data.get("languages", {}).keys())
    primary_language = languages[0] if languages else "multiple languages"
    
    top_deps = [d[0] for d in data.get("top_deps", [])[:3]]
    deps_str = list_to_english([f"`{d}`" for d in top_deps]) if top_deps else "standard libraries"
    
    eps = [ep["file"].split("/")[-1] for ep in data.get("entry_points", [])[:2]]
    eps_str = list_to_english([f"`{ep}`" for ep in eps]) if eps else "various internal scripts"
    
    return TPL_PROJECT_OVERVIEW.format(
        primary_language=primary_language,
        file_count=data.get("file_count", 0),
        class_count=data.get("class_count", 0),
        function_count=data.get("function_count", 0),
        top_deps=deps_str,
        entry_points=eps_str
    )

def generate_important_files_intro(files: list) -> str:
    if len(files) < 2:
        return "This project is very small; you can start reading anywhere."
        
    top_file = files[0]["score_data"]
    second_file = files[1]["score_data"]
    
    top_role = determine_file_role(top_file["filepath"], top_file["in_degree"], top_file["out_degree"], top_file["symbol_count"])
    second_role = determine_file_role(second_file["filepath"], second_file["in_degree"], second_file["out_degree"], second_file["symbol_count"])
    
    return TPL_IMPORTANT_FILES_INTRO.format(
        top_file=top_file["filepath"].split("/")[-1],
        top_role=top_role.lower(),
        second_file=second_file["filepath"].split("/")[-1],
        second_role=second_role.lower()
    )

def generate_file_detail_prose(file_data: dict) -> str:
    score_data = file_data.get("score_data", {})
    filepath = score_data.get("filepath", "unknown")
    in_degree = score_data.get("in_degree", 0)
    out_degree = score_data.get("out_degree", 0)
    symbol_count = score_data.get("symbol_count", 0)
    
    role = determine_file_role(filepath, in_degree, out_degree, symbol_count)
    
    return TPL_IMPORTANT_FILE_DETAIL.format(
        filepath=filepath.split("/")[-1],
        role=role.lower(),
        in_degree=in_degree,
        out_degree=out_degree
    )

def generate_data_model_prose(data: dict) -> str:
    entities = data.get("entities", [])
    if len(entities) < 2:
        return "This project does not have a complex object-oriented domain model with highly referenced entities."
        
    top = entities[0]
    second = entities[1]
    
    return TPL_DATA_MODEL.format(
        top_entity=top["name"],
        top_role=determine_file_role(top["file"], top["ref_count"], 0, 0).lower(),
        method_count=top["method_count"],
        second_entity=second["name"]
    )
    
def generate_call_flow_prose(flow: dict) -> str:
    ep = flow.get("ep", {})
    chains = flow.get("chains", [])
    
    callees = set()
    for c in chains:
        if c.get("callee"):
            callees.add(c["callee"].split(".")[-1])
            
    key_callees = list(callees)[:3]
    callees_str = list_to_english([f"`{c}`" for c in key_callees]) if key_callees else "internal utility functions"
    
    return TPL_CALL_FLOW.format(
        ep_name=ep.get("fqn", "main").split(".")[-1],
        ep_file=ep.get("file", "unknown").split("/")[-1],
        num_components=len(callees),
        key_callees=callees_str
    )

def generate_architecture_prose(data: dict) -> str:
    modules = data.get("modules", [])
    edges = data.get("edges", [])
    
    if not modules:
        return "The system is contained entirely in a single module."
        
    central_module = max(modules, key=lambda m: m.get("total_symbols", 0))
    
    return TPL_ARCHITECTURE.format(
        central_module=central_module.get("module_path", "root"),
        central_files=len(central_module.get("files", [])),
        edges_count=len(edges)
    )

def generate_module_guide_prose(module: dict) -> str:
    return TPL_MODULE_GUIDE.format(
        module_name=module.get("module_path", "root"),
        total_files=len(module.get("files", [])),
        total_symbols=module.get("total_symbols", 0)
    )

def generate_dependency_guide_prose(edge: dict) -> str:
    return TPL_DEPENDENCY_GUIDE.format(
        source_module=edge.get("source_module", "unknown"),
        target_module=edge.get("target_module", "unknown"),
        edge_count=edge.get("edge_count", 0)
    )

def generate_reading_guide_prose(data: dict) -> str:
    files = data.get("files", [])
    if len(files) < 2:
        return "Read the single file in this project."
        
    top_file = files[0]["filepath"].split("/")[-1]
    second_file = files[1]["filepath"].split("/")[-1]
    
    return TPL_READING_GUIDE.format(
        top_file=top_file,
        second_file=second_file
    )

def generate_project_map_prose(module: dict) -> str:
    langs = module.get("languages", [])
    langs_str = list_to_english(langs) if langs else "various languages"
    
    return TPL_PROJECT_MAP.format(
        module_path=module.get("module_path", "root"),
        file_count=len(module.get("files", [])),
        languages=langs_str
    )

def generate_glossary_prose(term: dict) -> str:
    raw_doc = term.get("docstring")
    doc_str = clean_docstring(raw_doc) if raw_doc else "Its specific purpose is implicitly defined by its usage."
    
    return TPL_GLOSSARY.format(
        term_name=term.get("name", "unknown"),
        file_path=term.get("file", "unknown").split("/")[-1],
        ref_count=term.get("incoming_refs", 0),
        docstring=doc_str
    )
