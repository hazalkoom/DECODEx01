import pytest
import os
import codelens_core

@pytest.fixture
def qa_repo(tmp_path):
    """A repository designed specifically to break the C++ language detector."""
    
    # 1. The Case-Sensitive Trickster
    # Developers often upload files from Windows where extensions get capitalized.
    cap_ext = tmp_path / "script.PY"
    cap_ext.write_text("print('hello')")
    
    # 2. The Deceptive Directory
    # What if a user names a FOLDER "my_component.js"? 
    # If we aren't careful, the C++ engine might think the folder is a JavaScript file.
    fake_dir = tmp_path / "sneaky.js"
    fake_dir.mkdir()
    
    # 3. The Sloppy Shebang (The string_view killer)
    # What if the developer put spaces after the #! or multiple spaces before 'node'?
    spaced_shebang = tmp_path / "spaced_out"
    spaced_shebang.write_text("#! /usr/bin/env    node\nconsole.log('hi')")
    
    # 4. The Windows Carriage Return (\r\n)
    # Files saved on Windows have different invisible line endings. Does our C++ slice it right?
    win_shebang = tmp_path / "win_script"
    win_shebang.write_bytes(b"#!/usr/bin/python3\r\nprint('windows')")
    
    # 5. The Tiny File Buffer Crash
    # We told C++ to read 256 bytes. What if the file is exactly 1 byte? Does the memory buffer crash?
    tiny_file = tmp_path / "tiny"
    tiny_file.write_text("#")
    
    return {
        "cap_ext": str(cap_ext),
        "fake_dir": str(fake_dir),
        "spaced_shebang": str(spaced_shebang),
        "win_shebang": str(win_shebang),
        "tiny": str(tiny_file)
    }


def test_qa_case_sensitivity(qa_repo):
    assert codelens_core.detect_language(qa_repo["cap_ext"]) == "Python", "Failed on capitalized extension"

def test_qa_deceptive_directory(qa_repo):
    # A folder should NEVER return a language, even if it has a .js extension.
    assert codelens_core.detect_language(qa_repo["fake_dir"]) == "Unknown", "Engine got tricked by a directory with an extension"

def test_qa_sloppy_shebangs(qa_repo):
    # Can our high-speed string_view parsing handle multiple spaces and weird formatting?
    assert codelens_core.detect_language(qa_repo["spaced_shebang"]) == "JavaScript", "Failed to parse sloppy shebang spaces"

def test_qa_windows_line_endings(qa_repo):
    # Did we successfully strip the \r before checking the hash map?
    assert codelens_core.detect_language(qa_repo["win_shebang"]) == "Python", "Failed on Windows \r\n line endings"

def test_qa_buffer_safety(qa_repo):
    # Proves our buffer doesn't segfault on 1-byte files
    assert codelens_core.detect_language(qa_repo["tiny"]) == "Unknown", "Crashed or misidentified a tiny 1-byte file"