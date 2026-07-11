import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))

from python.decode_db.query_api import DBQueryAPI

def run_tests():
    api = DBQueryAPI("decode_graph.db")

    print("\n🔍 1. Searching for the 'ASTParser' class definition...")
    symbols = api.find_symbol("ASTParser")
    for s in symbols:
        print(f"   -> Found {s['type']} in {s['file']} on line {s['line']}")

    print("\n📦 2. Searching for files that import 'pytest'...")
    deps = api.find_files_importing("pytest")
    for d in deps:
        print(f"   -> File: {d['file']} (Line {d['line']})")

    print("\n📄 3. Getting the outline of 'schema.py'...")
    outline = api.get_file_outline("schema.py")
    for item in outline:
        print(f"   -> {item['type'].capitalize()}: {item['name']} (Line {item['line']})")

if __name__ == "__main__":
    run_tests()