import os
from python.decode_docs.docs_generator import generate_docs

def test_generate_docs(populated_db, temp_db_path, tmp_path):
    output_dir = tmp_path / "docs"
    generate_docs(db_path=temp_db_path, project_root=".", output_dir=str(output_dir))
    
    assert output_dir.exists()
    assert (output_dir / "index.md").exists()
    
    # Verify all 11 documents are generated
    expected_files = [
        "PROJECT_OVERVIEW.md", "ARCHITECTURE.md", "MODULE_GUIDE.md",
        "DATA_FLOW.md", "DATA_MODEL.md", "READING_GUIDE.md",
        "IMPORTANT_FILES.md", "DEPENDENCY_GUIDE.md", "CALL_FLOW.md",
        "PROJECT_MAP.md", "GLOSSARY.md"
    ]
    for f in expected_files:
        assert (output_dir / f).exists()

    # Check contents of Project Overview
    with open(output_dir / "PROJECT_OVERVIEW.md", "r") as f:
        md_content = f.read()
        assert "Project Overview" in md_content
        assert "This repository is built primarily using" in md_content
