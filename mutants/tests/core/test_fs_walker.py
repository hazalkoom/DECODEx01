import os
import stat
import pytest
import codelens_core

@pytest.fixture
def complex_repo(tmp_path):
    """Creates a complex mock repository structure for testing."""
    
    # 1. Standard valid files
    (tmp_path / "main.py").write_text("print('hello')")
    (tmp_path / "README.md").write_text("# Test Repo")
    
    # 2. Ignored folders
    hidden_dir = tmp_path / ".git"
    hidden_dir.mkdir()
    (hidden_dir / "config").write_text("secret")
    
    node_dir = tmp_path / "node_modules"
    node_dir.mkdir()
    (node_dir / "lib.js").write_text("console.log('lib')")
    
    # 3. Deeply nested valid folder
    deep_dir = tmp_path / "src" / "api" / "v1"
    deep_dir.mkdir(parents=True)
    (deep_dir / "users.py").write_text("def get_users(): pass")
    
    # 4. Empty directory (should not cause crashes)
    empty_dir = tmp_path / "empty_assets"
    empty_dir.mkdir()

    # 5. Permission denied folder (Linux/macOS specific behavior)
    # We create a folder and then strip all read permissions from it.
    restricted_dir = tmp_path / "restricted_area"
    restricted_dir.mkdir()
    (restricted_dir / "secret.txt").write_text("you cannot see this")
    
    # Change permissions so the current user cannot read or execute inside it (chmod 000)
    # Note: This test works best on Unix systems. On Windows, permissions behave differently.
    if os.name != 'nt':
        os.chmod(restricted_dir, 0o000)

    yield str(tmp_path)

    # Cleanup: We must restore permissions to the restricted folder so pytest can delete the temp directory afterward!
    if os.name != 'nt':
        os.chmod(restricted_dir, stat.S_IRWXU)

def test_walker_comprehensive(complex_repo):
    discovered_files = codelens_core.walk_repository(complex_repo)
    filenames = [os.path.basename(f) for f in discovered_files]
    
    # --- Assertions ---
    
    # 1. Base files are found
    assert "main.py" in filenames
    assert "README.md" in filenames
    
    # 2. Deeply nested files are found
    assert "users.py" in filenames
    
    # 3. Ignored directories are skipped
    assert "config" not in filenames, "Failed to ignore .git"
    assert "lib.js" not in filenames, "Failed to ignore node_modules"
    
    # 4. Permission denied is handled gracefully (engine didn't crash)
    # And it didn't find the secret file inside
    assert "secret.txt" not in filenames, "Found file inside restricted folder"

def test_walker_nonexistent_directory():
    # Ensure the engine doesn't crash if given a path that doesn't exist at all
    discovered_files = codelens_core.walk_repository("/path/to/absolute/nowhere")
    assert len(discovered_files) == 0