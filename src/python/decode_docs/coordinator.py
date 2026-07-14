import os
from jinja2 import Environment, FileSystemLoader
from python.decode_db.query_api import DBQueryAPI

from .generators.project_overview import ProjectOverviewGenerator
from .generators.architecture import ArchitectureGenerator
from .generators.module_guide import ModuleGuideGenerator
from .generators.data_flow import DataFlowGenerator
from .generators.data_model import DataModelGenerator
from .generators.reading_guide import ReadingGuideGenerator
from .generators.important_files import ImportantFilesGenerator
from .generators.dependency_guide import DependencyGuideGenerator
from .generators.call_flow import CallFlowGenerator
from .generators.project_map import ProjectMapGenerator
from .generators.glossary import GlossaryGenerator

from .generators.setup_guide import SetupGuideGenerator

class DocsCoordinator:
    def __init__(self, db_path: str, output_dir: str, project_root: str = "."):
        self.api = DBQueryAPI(db_path)
        self.output_dir = output_dir
        self.project_root = project_root
        template_dir = os.path.join(os.path.dirname(__file__), "templates")
        self.env = Environment(loader=FileSystemLoader(template_dir))
        
        # Inject NLG functions into templates
        from .nlg.rules import (
            generate_project_overview_prose, generate_important_files_intro,
            generate_file_detail_prose, generate_data_model_prose,
            generate_call_flow_prose, generate_architecture_prose,
            generate_module_guide_prose, generate_dependency_guide_prose,
            generate_reading_guide_prose, generate_project_map_prose,
            generate_glossary_prose
        )
        self.env.globals["generate_project_overview_prose"] = generate_project_overview_prose
        self.env.globals["generate_important_files_intro"] = generate_important_files_intro
        self.env.globals["generate_file_detail_prose"] = generate_file_detail_prose
        self.env.globals["generate_data_model_prose"] = generate_data_model_prose
        self.env.globals["generate_call_flow_prose"] = generate_call_flow_prose
        self.env.globals["generate_architecture_prose"] = generate_architecture_prose
        self.env.globals["generate_module_guide_prose"] = generate_module_guide_prose
        self.env.globals["generate_dependency_guide_prose"] = generate_dependency_guide_prose
        self.env.globals["generate_reading_guide_prose"] = generate_reading_guide_prose
        self.env.globals["generate_project_map_prose"] = generate_project_map_prose
        self.env.globals["generate_glossary_prose"] = generate_glossary_prose
        
        self.generators = [
            SetupGuideGenerator(self.api, self.env, self.project_root),
            ProjectOverviewGenerator(self.api, self.env),
            ArchitectureGenerator(self.api, self.env),
            ModuleGuideGenerator(self.api, self.env),
            DataFlowGenerator(self.api, self.env),
            DataModelGenerator(self.api, self.env),
            ReadingGuideGenerator(self.api, self.env),
            ImportantFilesGenerator(self.api, self.env),
            DependencyGuideGenerator(self.api, self.env),
            CallFlowGenerator(self.api, self.env),
            ProjectMapGenerator(self.api, self.env),
            GlossaryGenerator(self.api, self.env),
        ]
        
    def generate_all(self) -> dict:
        generated = {}
        os.makedirs(self.output_dir, exist_ok=True)
        for gen in self.generators:
            filename = gen.generate(self.output_dir)
            if filename:
                generated[gen.title] = {"filename": filename, "question": gen.onboarding_question}
                
        self._render_index(generated)
        return generated
        
    def _render_index(self, generated: dict):
        template = self.env.get_template("index.md.jinja2")
        content = template.render(documents=generated)
        with open(os.path.join(self.output_dir, "index.md"), "w", encoding="utf-8") as f:
            f.write(content)
