from ..nlg.rules import *
from ..base_generator import BaseGenerator
from collections import defaultdict

class ProjectOverviewGenerator(BaseGenerator):
    output_filename = "PROJECT_OVERVIEW.md"
    template_name = "project_overview.md.jinja2"
    title = "Project Overview"
    onboarding_question = "What is this project?"
    
    def gather_data(self):
        files = self.api.get_all_files()
        symbols = self.api.get_all_symbols()
        refs = self.api.get_all_references()
        eps = self.api.get_entry_points()
        deps = self.api.get_all_dependencies()
        
        lang_counts = defaultdict(int)
        for f in files:
            lang_counts[f["language"]] += 1
            
        ext_deps = defaultdict(int)
        for d in deps:
            if not d["module_name"].startswith("."):
                ext_deps[d["module_name"]] += 1
        top_ext_deps = sorted(ext_deps.items(), key=lambda x: x[1], reverse=True)[:15]
        
        data = {
            "file_count": len(files),
            "class_count": sum(1 for s in symbols if s["type"] == "class"),
            "function_count": sum(1 for s in symbols if s["type"] in ["function", "method"]),
            "ref_count": len(refs),
            "languages": dict(lang_counts),
            "top_deps": top_ext_deps,
            "entry_points": eps
        }

        data['prose'] = generate_project_overview_prose(data)
        return data
