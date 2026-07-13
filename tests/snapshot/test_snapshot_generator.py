import os
import json
from python.decode_snapshot.snapshot_generator import generate_snapshot

def test_snapshot_generation(populated_db, temp_db_path, tmp_path):
    db_manager, _ = populated_db
    db_path = temp_db_path
    
    output_dir = tmp_path / ".decode"
    
    generate_snapshot(db_path=db_path, project_root=".", output_dir=str(output_dir))
    
    assert output_dir.exists()
    assert (output_dir / "SNAPSHOT.md").exists()
    assert (output_dir / "context").exists()
    
    with open(output_dir / "SNAPSHOT.md", "r") as f:
        md_content = f.read()
        assert "Total Files | 2" in md_content
        assert "Total Classes | 1" in md_content
        assert "Total Functions | 2" in md_content
        assert "Total References | 3" in md_content
        assert "/test/app.py" in md_content
        
    context_files = list((output_dir / "context").iterdir())
    assert len(context_files) == 2
    
    app_json_path = output_dir / "context" / "test_app.py.json"
    assert app_json_path.exists()
    
    with open(app_json_path, "r") as f:
        app_data = json.load(f)
        
    assert app_data["filepath"] == "/test/app.py"
    assert app_data["language"] == "python"
    assert len(app_data["symbols"]) == 2
    assert "os" in app_data["imports"]
    assert "pytest" in app_data["imports"]
    
    calls = app_data["calls"]
    assert len(calls) == 2
    assert any(c["from"] == "app.AppServer.start" and c["to"] == "utils.helper_func" for c in calls)
