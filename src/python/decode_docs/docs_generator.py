import os
from .coordinator import DocsCoordinator

def generate_docs(db_path: str = "decode_graph.db", project_root: str = ".", output_dir: str = "docs"):
    print(f"📚 Generating repository-agnostic onboarding documentation from {db_path}...")
    coordinator = DocsCoordinator(db_path, output_dir)
    generated = coordinator.generate_all()
    print(f"✅ Generated {len(generated)} onboarding documents in {output_dir}/")
