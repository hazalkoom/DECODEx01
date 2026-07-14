from ..nlg.rules import *
from ..base_generator import BaseGenerator

class ModuleGuideGenerator(BaseGenerator):
    output_filename = "MODULE_GUIDE.md"
    template_name = "module_guide.md.jinja2"
    title = "Module Guide"
    onboarding_question = "What does each module do?"
    
    def gather_data(self):
        modules = self.api.get_module_structure()
        for m in modules: m["prose"] = generate_module_guide_prose(m)
        return {"modules": modules}
