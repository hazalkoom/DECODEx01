import os
from python.decode_graphs.graph_generator import render_dependency_graph, render_call_graph, render_inheritance_graph

def test_dependency_graph(populated_db, temp_db_path, tmp_path):
    output_file = tmp_path / "graphs/dependency_graph.html"
    render_dependency_graph("app.py", db_path=temp_db_path, output_file=str(output_file))
    
    assert output_file.exists()
    
    with open(output_file, "r") as f:
        content = f.read()
        assert "app.py" in content
        assert "os" in content

def test_call_graph(populated_db, temp_db_path, tmp_path):
    output_file = tmp_path / "graphs/call_graph.html"
    render_call_graph("app.AppServer.start", db_path=temp_db_path, output_file=str(output_file))
    
    assert output_file.exists()
    
    with open(output_file, "r") as f:
        content = f.read()
        assert "app.AppServer.start" in content
        assert "utils.helper_func" in content

def test_inheritance_graph(populated_db, temp_db_path, tmp_path):
    output_file = tmp_path / "graphs/inheritance_graph.html"
    render_inheritance_graph(db_path=temp_db_path, output_file=str(output_file))
    
    assert output_file.exists()
    
    with open(output_file, "r") as f:
        content = f.read()
        assert "AppServer" in content
        assert "BaseServer" in content
