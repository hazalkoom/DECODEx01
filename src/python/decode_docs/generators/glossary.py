from ..nlg.rules import *
from ..base_generator import BaseGenerator

class GlossaryGenerator(BaseGenerator):
    output_filename = "GLOSSARY.md"
    template_name = "glossary.md.jinja2"
    title = "Glossary"
    onboarding_question = "What do project-specific terms mean?"
    
    def gather_data(self):
        terms = self.api.get_most_referenced_symbols(30)
        for t in terms: t["prose"] = generate_glossary_prose(t)
        return {"terms": terms}
