def determine_file_role(filepath: str, in_degree: int, out_degree: int, symbol_count: int) -> str:
    name = filepath.lower()
    
    # Heuristics based on naming conventions
    if "test" in name:
        return "Test Suite"
    if "utils" in name or "helpers" in name or "common" in name:
        return "Utility Library"
    if "model" in name or "schema" in name or "types" in name or "entity" in name:
        return "Data Model"
    if "controller" in name or "manager" in name or "orchestrator" in name or "handler" in name:
        return "Orchestrator"
    if "api" in name or "router" in name or "endpoint" in name:
        return "API Router"
    if "config" in name or "settings" in name or "env" in name:
        return "Configuration"
    if "db" in name or "database" in name or "repository" in name or "store" in name:
        return "Data Access Layer"
        
    # Heuristics based on graph metrics
    if in_degree == 0 and out_degree > 0:
        return "Entry Point"
    if in_degree > 5 and out_degree <= 2:
        return "Core Dependency"
    if out_degree > 5 and in_degree <= 2:
        return "Coordinator"
        
    return "Component"
