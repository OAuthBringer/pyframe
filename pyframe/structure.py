"""
Handles project structure creation
"""
import os
from jinja2 import Template
import yaml
from datetime import datetime
from pyframe import __project_root__, __templates__


class ProjectBuilder(object):
    """
    Handles new project creation.
    """

    def __init__(self, name, author, description, kwargs, templates=None,):
        self.name = name
        self.queue = [self.name, "tests/unit", "tests/integration"]
        self.paths = [os.path.join(name, elem) for elem in self.queue]
        self.paths.insert(0, name)
        self.kwargs=yaml.load(kwargs) if kwargs else {}
        self.config = dict(
            name=name,
            description=description,
            author=author,
            year=datetime.today().year,
            templates=templates,

        )

    def directories(self, name, paths):
        """
        Create whatever directories exist in the paths
        """

        if not os.path.exists(name):
            for path in paths:
                os.makedirs(path)
            return True
        return False


    def init(self, name, paths):
        """
        Create necesary __init__ files
        and add a __version__ to project
        __init__
        """
        for path in paths:
            open(os.path.join(path, "__init__.py"), 'a').close()
        open(os.path.join(name, name, "__init__.py"), "w").write("__version__ = '0.0.0'")
        return True

    def build_paths(self, name, path):
        """
        Create input/output paths for templates
        """
        return { 
            template: dict(
                input=os.path.join(path, template),
                output=os.path.join(name, template.split(".j2")[0]) 
            )
            for template in os.listdir(path)
            if template.endswith(".j2")
        } 

    def configure(self, name):
        """
        Hanldes template rendering
        and user defined templates.
        """
        templates = self.build_paths(name, __templates__)
        user_defined = self.config.get("templates")

        # User defined templates and arguments will
        # overwrite templates and cli params.
        if user_defined:
            templates.update(
                self.build_paths(name, user_defined))
            self.config.update(self.kwargs)

        for key in templates:
            input_path = templates[key]["input"]
            output_path = templates[key]["output"]
            if not os.path.exists(output_path):
                data = open(input_path, "r").read()
                open(output_path, "w").write(Template(data).render(**self.config))
            else:
                print("File '%s' already exists, skipping... " % output_path)
        
        state_file = open("%s/.pyframe" % name, "w")
        yaml.safe_dump(self.config, state_file, default_flow_style=False)
        return True

    def run(self):
        """
        Call ALL the methods!
        """
        self.directories(self.name, self.paths)
        self.init(self.name, self.paths)
        self.configure(self.name)

