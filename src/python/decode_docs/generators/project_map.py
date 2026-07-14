from ..nlg.rules import *
from ..base_generator import BaseGenerator

class ProjectMapGenerator(BaseGenerator):
    output_filename = "PROJECT_MAP.md"
    template_name = "project_map.md.jinja2"
    title = "Project Map"
    onboarding_question = "How is the repository laid out?"
    
    def gather_data(self):
        mods = self.api.get_module_structure()
        for m in mods: m["prose"] = generate_project_map_prose(m)
        return {"modules": mods}
