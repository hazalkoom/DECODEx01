from ..nlg.rules import *
from ..base_generator import BaseGenerator

class DataFlowGenerator(BaseGenerator):
    output_filename = "DATA_FLOW.md"
    template_name = "data_flow.md.jinja2"
    title = "Data Flow"
    onboarding_question = "How does information move?"
    
    def gather_data(self):
        eps = self.api.get_entry_points()
        workflows = []
        for ep in eps:
            chains = self.api.get_callee_chains(ep["fqn"], max_depth=3)
            if chains:
                workflows.append({"ep": ep, "chains": chains})
        for w in workflows: w["prose"] = generate_call_flow_prose(w)
        return {"workflows": workflows}
