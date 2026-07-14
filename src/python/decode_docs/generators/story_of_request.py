from ..base_generator import BaseGenerator
from ..nlg.story import find_deepest_call_chain, generate_story_prose, generate_story_mermaid

class StoryOfRequestGenerator(BaseGenerator):
    output_filename = "STORY_OF_A_REQUEST.md"
    template_name = "story_of_request.md.jinja2"
    title = "Story of a Request"
    onboarding_question = "What happens when the application runs?"

    def gather_data(self):
        chain = find_deepest_call_chain(self.api)
        return {
            "chain": chain,
            "prose": generate_story_prose(chain),
            "mermaid": generate_story_mermaid(chain),
        }
