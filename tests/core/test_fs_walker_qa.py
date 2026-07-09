import pytest
import os
import codelens_core

@pytest.fixture
def qa_walker_repo(tmp_path):
    """A repository designed to break the C++ File Walker."""
    
    # 1. The Abyss (Deep Nesting)
    # Does the recursive iterator blow the system's stack limit?
    deep_path = tmp_path
    for i in range(100):
        deep_path = deep_path / f"folder_{i}"
    deep_path.mkdir(parents=True)
    (deep_path / "treasure.txt").write_text("found it")
    
    # 2. The Infinite Loop (Symlink)
    # If the walker blindly follows symlinks, a link pointing to its parent 
    # will cause an infinite loop until the memory crashes.
    loop_dir = tmp_path / "symlink_trap"
    loop_dir.mkdir()
    (loop_dir / "safe.txt").write_text("hello")
    
    if os.name != 'nt':  # Symlinks require special privileges on Windows, so we only test on Unix
        os.symlink(loop_dir, loop_dir / "infinite")
        
    return str(tmp_path)

def test_qa_walker_deep_nesting(qa_walker_repo):
    discovered = codelens_core.walk_repository(qa_walker_repo)
    filenames = [os.path.basename(f) for f in discovered]
    assert "treasure.txt" in filenames, "Walker failed to reach deeply nested files"

def test_qa_walker_infinite_symlink(qa_walker_repo):
    if os.name == 'nt':
        pytest.skip("Skipping symlink test on Windows")
        
    # If this test doesn't hang forever or crash with a stack overflow, 
    # it means our C++ iterator correctly avoids following symlinks by default!
    discovered = codelens_core.walk_repository(qa_walker_repo)
    filenames = [os.path.basename(f) for f in discovered]
    
    assert "safe.txt" in filenames
    # We should only find safe.txt ONCE. If it followed the loop, it would find it infinitely.
    assert filenames.count("safe.txt") == 1