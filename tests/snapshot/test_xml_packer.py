import os
import xml.etree.ElementTree as ET
from python.decode_snapshot.snapshot_generator import (
    generate_xml_bundle,
    generate_focused_xml_bundle,
    update_session_memory
)

def test_xml_packer_global_and_focused(populated_db, temp_db_path, tmp_path):
    db_manager, _ = populated_db
    db_path = temp_db_path
    
    xml_output = tmp_path / "CONTEXT_BUNDLE.xml"
    focused_output = tmp_path / "FOCUSED_CONTEXT.xml"
    status_md = tmp_path / "STATUS.md"
    
    # 1. Test update_session_memory
    update_session_memory(db_path=db_path, status_md_path=str(status_md))
    assert status_md.exists()
    with open(status_md, "r", encoding="utf-8") as f:
        status_text = f.read()
        assert "# DECODE Workspace Status & Session Memory" in status_text
        assert "Verification & Health" in status_text
        assert "2 files" in status_text
        
    # 2. Test generate_xml_bundle
    generate_xml_bundle(db_path=db_path, output_path=str(xml_output))
    assert xml_output.exists()
    
    # Verify XML structure and content
    tree = ET.parse(xml_output)
    root = tree.getroot()
    assert root.tag == "codebase_context"
    
    session_status = root.find("session_status")
    assert session_status is not None
    assert "DECODE Workspace Status" in session_status.text
    
    stats = root.find("project_summary")
    assert stats is not None
    assert stats.find("total_files").text == "2"
    assert stats.find("total_classes").text == "1"
    
    files = root.find("files")
    assert files is not None
    file_elements = files.findall("file")
    assert len(file_elements) == 2
    
    app_file = next(f for f in file_elements if f.get("path") == "/test/app.py")
    assert app_file.get("language") == "python"
    
    symbols = app_file.find("symbols")
    assert symbols is not None
    symbol_elements = symbols.findall("symbol")
    assert len(symbol_elements) == 2
    assert any(s.get("name") == "AppServer" and s.get("kind") == "class" for s in symbol_elements)
    
    # 3. Test generate_focused_xml_bundle focusing on "app"
    generate_focused_xml_bundle(
        db_path=db_path,
        target_file="app",
        output_path=str(focused_output),
        max_depth=1
    )
    assert focused_output.exists()
    
    ftree = ET.parse(focused_output)
    froot = ftree.getroot()
    assert froot.tag == "codebase_context"
    
    ffiles = froot.find("files")
    assert ffiles is not None
    ffile_elements = ffiles.findall("file")
    # Should include app.py and utils.py since they are linked in populated_db
    assert len(ffile_elements) >= 1
