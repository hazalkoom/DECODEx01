import pytest
import codelens_core

@pytest.fixture
def language_repo(tmp_path):
    # 1. Standard extension files
    py_file = tmp_path / "server.py"
    py_file.write_text("print('hello')")
    
    md_file = tmp_path / "README.md"
    md_file.write_text("# Project")
    
    # 2. Shebangs (Testing our new high-speed string_view parsing)
    cli_py = tmp_path / "my_cli_tool"
    cli_py.write_text("#!/usr/bin/env python3\nprint('starting cli')")
    
    cli_bash = tmp_path / "deploy_script"
    cli_bash.write_text("#!/bin/bash\necho 'deploying'")
    
    # 3. Magic Bytes (Testing binary file detection without extensions)
    fake_pdf = tmp_path / "mystery_doc"
    fake_pdf.write_text("%PDF-1.4\nSome binary junk")
    
    fake_zip = tmp_path / "archive"
    fake_zip.write_text("PK\x03\x04\nzipped data")

    return {
        "python": str(py_file),
        "markdown": str(md_file),
        "shebang_py": str(cli_py),
        "shebang_bash": str(cli_bash),
        "magic_pdf": str(fake_pdf),
        "magic_zip": str(fake_zip)
    }

def test_language_detection(language_repo):
    # Extensions
    assert codelens_core.detect_language(language_repo["python"]) == "Python"
    assert codelens_core.detect_language(language_repo["markdown"]) == "Markdown"
    
    # Shebangs
    assert codelens_core.detect_language(language_repo["shebang_py"]) == "Python"
    assert codelens_core.detect_language(language_repo["shebang_bash"]) == "Shell"
    
    # Magic Bytes
    assert codelens_core.detect_language(language_repo["magic_pdf"]) == "PDF Document"
    assert codelens_core.detect_language(language_repo["magic_zip"]) == "ZIP/Office Archive"