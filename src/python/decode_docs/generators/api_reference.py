from ..base_generator import BaseGenerator
from ..nlg.scanners.api_scanner import scan_api_routes
from ..nlg.few_shot.schema import load_schema, populate_sections

class ApiReferenceGenerator(BaseGenerator):
    output_filename = "API.md"
    template_name = "api.md.jinja2"
    title = "API Reference"
    onboarding_question = "What endpoints does this project expose?"

    def __init__(self, query_api, template_env, project_root="."):
        super().__init__(query_api, template_env)
        self.project_root = project_root

    def should_generate(self):
        routes = scan_api_routes(self.api)
        return len(routes) > 0

    def gather_data(self):
        routes = scan_api_routes(self.api)
        schema = load_schema(self.project_root)
        sections = populate_sections(schema, self.api)
        return {"routes": routes, "sections": sections}
