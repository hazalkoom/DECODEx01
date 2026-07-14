from ..base_generator import BaseGenerator
from ..nlg.scanners.root_scanner import scan_project_root

class SetupGuideGenerator(BaseGenerator):
    output_filename = "SETUP.md"
    template_name = "setup.md.jinja2"
    title = "Setup Guide"
    onboarding_question = "How do I get this project running?"

    def __init__(self, query_api, template_env, project_root="."):
        super().__init__(query_api, template_env)
        self.project_root = project_root

    def gather_data(self):
        return scan_project_root(self.project_root)
