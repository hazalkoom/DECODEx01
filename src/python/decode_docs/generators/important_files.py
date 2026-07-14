from ..nlg.rules import *
from ..base_generator import BaseGenerator

class ImportantFilesGenerator(BaseGenerator):
    output_filename = "IMPORTANT_FILES.md"
    template_name = "important_files.md.jinja2"
    title = "Important Files"
    onboarding_question = "Which files should I understand first?"
    
    def gather_data(self):
        scores = self.api.get_file_importance_scores()[:20]
        details = []
        for s in scores:
            details.append({"score_data": s, "detail": self.api.get_file_detail(s["filepath"])})
        intro = generate_important_files_intro(details)
        for d in details: d["prose"] = generate_file_detail_prose(d)
        return {"files": details, "intro_prose": intro}
