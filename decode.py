import argparse
import sys
import subprocess

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
    graph_parser.add_argument("target", help="The file or module to map dependencies for")

    # Parse the arguments typed in the terminal
    args = parser.parse_args()

    # Route the commands
    if args.command == "index":
        print(f"🚀 Triggering Smart Indexer on: {args.path}")
        # For now, we just call the script the agent moved to the scripts folder
        subprocess.run(["poetry", "run", "python", "scripts/run_indexer.py", args.path])
        
    elif args.command == "query":
        print(f"🔍 Querying database for: '{args.symbol}'")
        from src.python.decode_db.query_api import DBQueryAPI
        api = DBQueryAPI("decode_graph.db")
        results = api.find_symbol(args.symbol)
        if not results:
            print("   ❌ Symbol not found.")
        for r in results:
            print(f"   ✅ Found {r['type']} in {r['file']} on line {r['line']}")
            
    elif args.command == "graph":
        print(f"🕸️  Tracing deep dependency tree for: {args.target}")
        from sqlalchemy import create_engine, text
        from pyvis.network import Network
        
        engine = create_engine("sqlite:///decode_graph.db")
        
        with engine.connect() as conn:
            # THE RECURSIVE CTE
            query = text("""
                WITH RECURSIVE dep_tree AS (
                    SELECT 
                        f.filepath AS source_file, 
                        d.module_name AS imported_module, 
                        1 AS depth
                    FROM files f
                    JOIN dependencies d ON f.id = d.file_id
                    WHERE f.filepath LIKE :target
                    
                    UNION
                    
                    SELECT 
                        f.filepath, 
                        d.module_name, 
                        dt.depth + 1
                    FROM files f
                    JOIN dependencies d ON f.id = d.file_id
                    JOIN dep_tree dt 
                        ON f.filepath LIKE '%' || replace(dt.imported_module, '.', '/') || '.py'
                    WHERE dt.depth < 5
                )
                SELECT DISTINCT source_file, imported_module, depth 
                FROM dep_tree 
                ORDER BY depth, source_file;
            """)
            
            results = conn.execute(query, {"target": f"%{args.target}%"}).fetchall()
            
            if not results:
                print("   ❌ No dependencies found.")
            else:
                print("🎨 Generating strictly hierarchical architecture map...")
                
                # Setup a dark-mode canvas
                net = Network(height="800px", width="100%", bgcolor="#1e1e1e", font_color="white", directed=True)
                
                # FORCE A PROFESSIONAL TOP-DOWN TREE LAYOUT
                net.set_options("""
                var options = {
                  "layout": {
                    "hierarchical": {
                      "enabled": true,
                      "direction": "UD",
                      "sortMethod": "directed",
                      "levelSeparation": 150,
                      "nodeSpacing": 150
                    }
                  },
                  "physics": {
                    "hierarchicalRepulsion": {
                      "nodeDistance": 150
                    }
                  },
                  "edges": {
                    "smooth": {
                      "type": "cubicBezier",
                      "forceDirection": "vertical",
                      "roundness": 0.4
                    }
                  }
                }
                """)
                
                # Track what we've added to avoid Pyvis duplicate node errors
                added_nodes = set()
                
                for source, module, depth in results:
                    clean_source = source.split('/')[-1]
                    
                    # 1. Add the Source File Node
                    if clean_source not in added_nodes:
                        net.add_node(clean_source, label=clean_source, color="#E53935", shape="box", font={"face": "monospace", "size": 16})
                        added_nodes.add(clean_source)
                    
                    # 2. Add the Target Module Node
                    if module not in added_nodes:
                        # If it's a standard library or third-party (like os, pytest, sqlalchemy), make it small and gray
                        if not module.startswith('.') and "decode" not in module and "schema" not in module:
                            net.add_node(module, label=module, color="#424242", shape="dot", size=10, font={"size": 10, "color": "gray"})
                        else:
                            # Internal project files get the premium purple highlight
                            net.add_node(module, label=module, color="#8E24AA", shape="box", font={"face": "monospace", "size": 16})
                        added_nodes.add(module)
                        
                    # 3. Draw the connection
                    net.add_edge(clean_source, module, color="#555555")

                output_file = "architecture_map.html"
                net.save_graph(output_file)
                
                print(f"✅ Premium hierarchical graph saved to: {output_file}")

if __name__ == "__main__":
    main()