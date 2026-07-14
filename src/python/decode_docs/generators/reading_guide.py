from ..nlg.rules import *
from ..base_generator import BaseGenerator

class ReadingGuideGenerator(BaseGenerator):
    output_filename = "READING_GUIDE.md"
    template_name = "reading_guide.md.jinja2"
    title = "Reading Guide"
    onboarding_question = "Where should I start reading?"
    
    def gather_data(self):
        scores = self.api.get_file_importance_scores()
        data = {"files": scores[:15]}
        data["prose"] = generate_reading_guide_prose(data)
        return data
