import os
import time
import pytest
import threading
import tempfile
import codelens_core

# 1. Type Safety & Negative Tests
def test_negative_invalid_types():
    """
    Ensure the C++ bindings enforce type limits and raise proper Python exceptions.
    """
    parser = codelens_core.ASTParser()
    
    # Passing non-string to set_language should raise TypeError
    with pytest.raises(TypeError):
        parser.set_language(123) # type: ignore
        
    with pytest.raises(TypeError):
        parser.set_language(None) # type: ignore

    # Passing non-string to extract_symbols
    with pytest.raises(TypeError):
        parser.extract_symbols(None) # type: ignore

    # Passing non-string to walk_repository
    with pytest.raises(TypeError):
        codelens_core.walk_repository(None) # type: ignore

    # Passing non-string to detect_language
    with pytest.raises(TypeError):
        codelens_core.detect_language(None) # type: ignore

# 2. Large / Deep Stress Tests
def test_large_file_ast_stress():
    """
    Ensure the parser doesn't overflow stack or memory when parsing massive files
    with a large number of structures.
    """
    parser = codelens_core.ASTParser()
    assert parser.set_language("python") is True

    # 1. Flat sequential functions (Stress-tests memory/speed for large counts)
    flat_py = []
    for i in range(2000):
        flat_py.append(f"def func_{i}():\n    pass\n")
    flat_py_str = "\n".join(flat_py)

    start_time = time.time()
    symbols = parser.extract_symbols(flat_py_str)
    duration = time.time() - start_time
    
    assert len(symbols) == 2000
    assert duration < 5.0, f"Flat AST parsing took too long: {duration:.2f}s"

    # 2. Deeply nested functions (Tests recursion safety up to tree-sitter's internal limits)
    indent = ""
    nested_py = []
    for i in range(30):
        nested_py.append(f"{indent}def func_{i}():")
        indent += "    "
    nested_py.append(f"{indent}pass")
    nested_py_str = "\n".join(nested_py)

    start_time = time.time()
    symbols_nested = parser.extract_symbols(nested_py_str)
    duration_nested = time.time() - start_time
    
    assert len(symbols_nested) == 30
    assert duration_nested < 2.0, f"Nested AST parsing took too long: {duration_nested:.2f}s"

    # Construct a very large Python string with 10000 imports (approx 5MB file)
    large_py_str = "\n".join([f"import module_{i}" for i in range(50000)])
    
    start_time = time.time()
    deps = parser.extract_dependencies(large_py_str)
    duration = time.time() - start_time
    
    assert len(deps) == 50000
    assert duration < 10.0, f"Large file AST parsing took too long: {duration:.2f}s"

# 3. Concurrency / Race Conditions
def test_walker_concurrency_race():
    """
    Start the walker in a directory while another thread constantly adds and
    deletes files. The walker should not crash (segfault) and should complete.
    """
    stop_event = threading.Event()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Pre-populate some files
        for i in range(10):
            with open(os.path.join(tmpdir, f"file_{i}.py"), "w") as f:
                f.write("print('hello')")
                
        def file_mutator():
            counter = 0
            while not stop_event.is_set():
                # Add file
                new_file = os.path.join(tmpdir, f"temp_{counter}.py")
                try:
                    with open(new_file, "w") as f:
                        f.write("# temp file")
                    # Delete another file
                    del_file = os.path.join(tmpdir, f"temp_{counter - 1}.py")
                    if os.path.exists(del_file):
                        os.remove(del_file)
                except OSError:
                    pass
                counter += 1
                time.sleep(0.001)

        mutator_thread = threading.Thread(target=file_mutator)
        mutator_thread.start()

        try:
            # Walk directory multiple times to trigger potential race conditions in filesystem access
            for _ in range(20):
                files = codelens_core.walk_repository(tmpdir)
                assert len(files) >= 10 # at least the base files are there
        finally:
            stop_event.set()
            mutator_thread.join()
