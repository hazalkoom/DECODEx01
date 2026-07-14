from ..nlg.rules import *
from ..base_generator import BaseGenerator

class DataModelGenerator(BaseGenerator):
    output_filename = "DATA_MODEL.md"
    template_name = "data_model.md.jinja2"
    title = "Data Model"
    onboarding_question = "What are the important concepts?"
    
    def gather_data(self):
        entities = self.api.get_domain_entities()
        hierarchy = self.api.get_class_hierarchy_full()
        data = {"entities": entities, "hierarchy": hierarchy}
        data["prose"] = generate_data_model_prose(data)
        return data
