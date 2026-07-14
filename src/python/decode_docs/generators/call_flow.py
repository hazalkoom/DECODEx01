from ..nlg.rules import *
from ..base_generator import BaseGenerator

class CallFlowGenerator(BaseGenerator):
    output_filename = "CALL_FLOW.md"
    template_name = "call_flow.md.jinja2"
    title = "Call Flow"
    onboarding_question = "What happens during execution?"
    
    def gather_data(self):
        eps = self.api.get_entry_points()
        flows = []
        for ep in eps:
            chains = self.api.get_callee_chains(ep["fqn"], max_depth=4)
            if chains:
                flows.append({"ep": ep, "chains": chains})
        for f in flows: f["prose"] = generate_call_flow_prose(f)
        return {"flows": flows}
