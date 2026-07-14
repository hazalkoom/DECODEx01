import os
from sqlalchemy import create_engine, text
from pyvis.network import Network

def _create_network() -> Network:
    net = Network(height="100%", width="100%", bgcolor="#0a0e14", font_color="#e6edf3", directed=True)
    template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates", "graph_template.html"))
    net.set_template(template_path)
    return net

def _get_file_tooltip(filename: str, conn) -> str:
    query = text("""
        SELECT s.name, s.type, s.signature 
        FROM symbols s
        JOIN files f ON s.file_id = f.id
        WHERE f.filepath LIKE '%' || :filename
    """)
    symbols = conn.execute(query, {"filename": filename}).fetchall()
    if not symbols:
        return f"File: {filename}<br>No symbols found or external module."
    lines = [f"<h3>File Outline: {filename}</h3><ul>"]
    for name, kind, sig in symbols:
        sig_str = f" ({sig})" if sig else ""
        lines.append(f"<li><b>{kind}:</b> {name}{sig_str}</li>")
    lines.append("</ul>")
    return "".join(lines)

def _get_symbol_tooltip(fqn: str, conn) -> str:
    query = text("""
        SELECT signature, return_type, docstring 
        FROM symbols 
        WHERE fully_qualified_name = :fqn OR name = :fqn
        LIMIT 1
    """)
    res = conn.execute(query, {"fqn": fqn}).fetchone()
    if not res:
        return f"External or unresolved symbol: {fqn}"
    sig, ret, doc = res
    ret_str = f" -> {ret}" if ret else ""
    doc_str = doc if doc else "No documentation available."
    return f"<b>Signature:</b> {sig or fqn}{ret_str}<br><br><b>Docstring:</b><br>{doc_str}"

def _get_class_tooltip(classname: str, conn) -> str:
    query = text("""
        SELECT docstring 
        FROM symbols 
        WHERE name = :name AND type = 'class'
        LIMIT 1
    """)
    res = conn.execute(query, {"name": classname}).fetchone()
    if not res:
        return f"External or unresolved class: {classname}"
    doc = res[0]
    return doc if doc else "No documentation available."

def render_dependency_graph(target: str, db_path: str = "decode_graph.db", output_file: str = ".decode/graphs/dependency_graph.html"):
    print(f"🕸️  Tracing deep dependency tree for: {target}")
    engine = create_engine(f"sqlite:///{db_path}")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with engine.connect() as conn:
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
        
        results = conn.execute(query, {"target": f"%{target}%"}).fetchall()
        
        if not results:
            print("   ❌ No dependencies found.")
            return
            
        print("🎨 Generating strictly hierarchical architecture map...")
        net = _create_network()
        added_nodes = set()
        
        for source, module, depth in results:
            clean_source = source.split('/')[-1]
            
            if clean_source not in added_nodes:
                tooltip = _get_file_tooltip(clean_source, conn)
                group = "entry" if clean_source.lower() == target.lower() or target.lower() in clean_source.lower() else "file"
                net.add_node(clean_source, label=clean_source, title=tooltip, group=group)
                added_nodes.add(clean_source)
            
            if module not in added_nodes:
                tooltip = _get_file_tooltip(module, conn)
                if not module.startswith('.') and "decode" not in module and "schema" not in module:
                    net.add_node(module, label=module, title=tooltip, group="external")
                else:
                    net.add_node(module, label=module, title=tooltip, group="file")
                added_nodes.add(module)
                
            net.add_edge(clean_source, module, color="#555555")

        net.save_graph(output_file)
        print(f"✅ Premium dependency graph saved to: {output_file}")

def render_call_graph(symbol: str, db_path: str = "decode_graph.db", output_file: str = ".decode/graphs/call_graph.html"):
    print(f"🕸️  Tracing call graph for symbol: {symbol}")
    engine = create_engine(f"sqlite:///{db_path}")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with engine.connect() as conn:
        query = text("""
            SELECT caller_fqn, callee_fqn, kind
            FROM "references"
            WHERE (caller_fqn = :symbol OR callee_fqn = :symbol)
              AND kind = 'Call'
        """)
        
        results = conn.execute(query, {"symbol": symbol}).fetchall()
        
        if not results:
            print("   ❌ No calls found for this symbol.")
            return
            
        print("🎨 Generating call graph...")
        net = _create_network()
        added_nodes = set()
        
        for caller, callee, kind in results:
            if caller not in added_nodes:
                group = "entry" if caller == symbol else "symbol"
                tooltip = _get_symbol_tooltip(caller, conn)
                net.add_node(caller, label=caller, title=tooltip, group=group)
                added_nodes.add(caller)
                
            if callee not in added_nodes:
                group = "entry" if callee == symbol else "symbol"
                tooltip = _get_symbol_tooltip(callee, conn)
                net.add_node(callee, label=callee, title=tooltip, group=group)
                added_nodes.add(callee)
                
            net.add_edge(caller, callee, color="#aaaaaa")

        net.save_graph(output_file)
        print(f"✅ Call graph saved to: {output_file}")

def render_inheritance_graph(db_path: str = "decode_graph.db", output_file: str = ".decode/graphs/inheritance_graph.html"):
    print("🕸️  Tracing project-wide inheritance graph")
    engine = create_engine(f"sqlite:///{db_path}")
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with engine.connect() as conn:
        query = text("""
            SELECT caller_fqn, callee_fqn
            FROM "references"
            WHERE kind = 'Inheritance'
        """)
        
        results = conn.execute(query).fetchall()
        
        if not results:
            print("   ❌ No inheritance relationships found.")
            return
            
        print("🎨 Generating inheritance graph...")
        net = _create_network()
        added_nodes = set()
        
        for child, parent in results:
            if parent not in added_nodes:
                tooltip = _get_class_tooltip(parent, conn)
                net.add_node(parent, label=parent, title=tooltip, group="class")
                added_nodes.add(parent)
                
            if child not in added_nodes:
                tooltip = _get_class_tooltip(child, conn)
                net.add_node(child, label=child, title=tooltip, group="class")
                added_nodes.add(child)
                
            net.add_edge(parent, child, color="#aaaaaa", label="inherits")

        net.save_graph(output_file)
        print(f"✅ Inheritance graph saved to: {output_file}")
