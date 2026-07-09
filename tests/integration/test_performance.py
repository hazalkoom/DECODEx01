import os
import tempfile
import codelens_core

def test_ast_parsing_benchmark(benchmark):
    """
    Benchmark python symbols extraction.
    """
    parser = codelens_core.ASTParser()
    parser.set_language("python")
    
    # 500 lines of typical Python code
    python_code = "\n".join([
        f"class Client_{i}:\n"
        f"    def method_{i}(self):\n"
        f"        return {i}\n"
        for i in range(100)
    ])
    
    # Run benchmark
    symbols = benchmark(parser.extract_symbols, python_code)
    assert len(symbols) == 200 # 100 classes + 100 methods

def test_walk_repository_benchmark(benchmark):
    """
    Benchmark walking a repository structure.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a tree with 500 files
        for i in range(50):
            sub = os.path.join(tmpdir, f"sub_{i}")
            os.mkdir(sub)
            for j in range(10):
                with open(os.path.join(sub, f"file_{j}.py"), "w") as f:
                    f.write("print('hello')")
                    
        files = benchmark(codelens_core.walk_repository, tmpdir)
        assert len(files) == 500
