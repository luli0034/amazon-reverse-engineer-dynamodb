# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from jinja2 import Environment, FileSystemLoader
import os
class CreateScript:
    """
        Generates model classes
    """
    def __init__(self, filepath, code):  
        self.filepath = filepath
        self.script_code = code

    def create_file(self):
        """
        Create a file

        Returns:
            _type_: None
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            file.write(self.script_code)

        return None


class GenerateModel:
    """
        Generates model classes
    """

    def __init__(self, template_location):
        file_loader = FileSystemLoader(template_location)
        env = Environment(loader=file_loader, autoescape=True)
        self.template = env.get_template('model.jinja')

    def render_template(self, table_attributes, filepath):
        """
            Renders template

        Args:
            table_attributes (dict): Table attributes
        """

        output = self.template.render(table_attributes=table_attributes)
        script = CreateScript(filepath, output)
        script.create_file()
