from ..nlg.rules import *
from ..base_generator import BaseGenerator

class DependencyGuideGenerator(BaseGenerator):
    output_filename = "DEPENDENCY_GUIDE.md"
    template_name = "dependency_guide.md.jinja2"
    title = "Dependency Guide"
    onboarding_question = "What depends on what?"
    
    def gather_data(self):
        edges = self.api.get_cross_module_edges()
        for e in edges: e["prose"] = generate_dependency_guide_prose(e)
        return {"edges": edges}
