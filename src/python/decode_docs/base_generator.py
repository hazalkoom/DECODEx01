import os
import json
from typing import Optional, Dict, Any
from jinja2 import Environment
from python.decode_db.query_api import DBQueryAPI

class BaseGenerator:
    output_filename: str = ""
    template_name: str = ""
    title: str = ""
    onboarding_question: str = ""
    
    def __init__(self, query_api: DBQueryAPI, template_env: Environment):
        self.api = query_api
        self.env = template_env
    
    def gather_data(self) -> Dict[str, Any]:
        raise NotImplementedError
    
    def should_generate(self) -> bool:
        return True
    
    def generate(self, output_dir: str) -> Optional[str]:
        if not self.should_generate():
            return None
        data = self.gather_data()
        template = self.env.get_template(self.template_name)
        content = template.render(**data)
        
        output_path = os.path.join(output_dir, self.output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return self.output_filename
