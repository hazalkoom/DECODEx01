from ..nlg.rules import *
from ..base_generator import BaseGenerator

class ArchitectureGenerator(BaseGenerator):
    output_filename = "ARCHITECTURE.md"
    template_name = "architecture.md.jinja2"
    title = "Architecture"
    onboarding_question = "How is it organized?"
    
    def gather_data(self):
        modules = self.api.get_module_structure()
        edges = self.api.get_cross_module_edges()
        data = {"modules": modules, "edges": edges}
        data["prose"] = generate_architecture_prose(data)
        return data
