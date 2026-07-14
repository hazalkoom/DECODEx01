import argparse
import sys
import subprocess
import os

# Ensure src/ is in the pythonpath so module imports work like they do in pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

def main():
    # Setup the main CLI parser
    parser = argparse.ArgumentParser(
        description="DECODE: High-Speed Local Code Intelligence Engine",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Command 1: decode index
    index_parser = subparsers.add_parser("index", help="Scan the project and update the SQLite database")
    index_parser.add_argument("path", nargs="?", default=".", help="Path to index (default: current directory)")

    # Command 2: decode query
    query_parser = subparsers.add_parser("query", help="Instantly find where a class or function is defined")
    query_parser.add_argument("symbol", help="The name of the class or function to find")

    # Command 3: decode graph (Our upcoming Sandbox!)
    graph_parser = subparsers.add_parser("graph", help="Generate a visual dependency graph using Raw SQL")
    graph_parser.add_argument("--type", choices=["deps", "calls", "inheritance"], default="deps")
    graph_parser.add_argument("target", nargs="?", default=None, help="The file or module to map dependencies for")
    graph_parser.add_argument("--db", default="decode_graph.db", help="Path to the SQLite database")

    # Command 4: decode snapshot
    snap_parser = subparsers.add_parser("snapshot", help="Generate AI-friendly .decode/ context folder from the indexed DB")
    snap_parser.add_argument("--output", default=".decode", help="Output directory (default: .decode)")
    snap_parser.add_argument("--db", default="decode_graph.db", help="Path to the SQLite database")

    # Command 5: decode docs
    docs_parser = subparsers.add_parser("docs", help="Generate Markdown documentation from the indexed database")
    docs_parser.add_argument("--output", default="docs", help="Output directory (default: docs)")
    docs_parser.add_argument("--db", default="decode_graph.db", help="Path to the SQLite database")
    docs_parser.add_argument("--ai", action="store_true", help="Use AI to generate high-quality human-readable docs (requires API key)")
    docs_parser.add_argument("--root", default=".", help="Project root path to scan config files for CONTRIBUTING.md (default: .)")

    # Command 6: decode pack
    pack_parser = subparsers.add_parser("pack", help="Consolidate the codebase snapshot and status memory into a single CONTEXT_BUNDLE.xml file")
    pack_parser.add_argument("--output", default=".decode/CONTEXT_BUNDLE.xml", help="Output file path")
    pack_parser.add_argument("--db", default="decode_graph.db", help="Path to the SQLite database")

    # Command 7: decode context
    context_parser = subparsers.add_parser("context", help="Generate a focused XML context bundle mapping the dependencies of a target file")
    context_parser.add_argument("--focus", required=True, help="Target file name or path to focus the context on")
    context_parser.add_argument("--output", default=".decode/FOCUSED_CONTEXT.xml", help="Output file path")
    context_parser.add_argument("--db", default="decode_graph.db", help="Path to the SQLite database")
    context_parser.add_argument("--depth", type=int, default=2, help="Recursive traversal depth (default: 2)")

    # Parse the arguments typed in the terminal
    args = parser.parse_args()

    # Route the commands
    if args.command == "index":
        print(f"🚀 Triggering Smart Indexer on: {args.path}")
        # For now, we just call the script the agent moved to the scripts folder
        subprocess.run(["poetry", "run", "python", "scripts/run_indexer.py", args.path])
        
    elif args.command == "query":
        print(f"🔍 Querying database for: '{args.symbol}'")
        from python.decode_db.query_api import DBQueryAPI
        api = DBQueryAPI("decode_graph.db")
        results = api.find_symbol(args.symbol)
        if not results:
            print("   ❌ Symbol not found.")
        for r in results:
            print(f"   ✅ Found {r['type']} in {r['file']} on line {r['line']}")
    elif args.command == "snapshot":
        from python.decode_snapshot.snapshot_generator import generate_snapshot
        generate_snapshot(args.db, ".", args.output)

    elif args.command == "docs":
        if args.ai:
            from python.decode_docs.ai.ai_docs_generator import generate_ai_docs
            generate_ai_docs(args.db, args.root, args.output)
        else:
            from python.decode_docs.docs_generator import generate_docs
            generate_docs(args.db, ".", args.output)
            
    elif args.command == "graph":
        from python.decode_graphs.graph_generator import render_dependency_graph, render_call_graph, render_inheritance_graph
        if args.type == "deps":
            if not args.target:
                print("❌ Target is required for dependency graph")
                sys.exit(1)
            render_dependency_graph(args.target, args.db)
        elif args.type == "calls":
            if not args.target:
                print("❌ Target (symbol) is required for call graph")
                sys.exit(1)
            render_call_graph(args.target, args.db)
        elif args.type == "inheritance":
            render_inheritance_graph(args.db)

    elif args.command == "pack":
        from python.decode_snapshot.snapshot_generator import generate_xml_bundle
        generate_xml_bundle(args.db, args.output)

    elif args.command == "context":
        from python.decode_snapshot.snapshot_generator import generate_focused_xml_bundle
        generate_focused_xml_bundle(args.db, args.focus, args.output, args.depth)

if __name__ == "__main__":
    main()