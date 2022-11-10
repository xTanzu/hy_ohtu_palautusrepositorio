from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url
    
    def print_recursive(self, element: dict, level: int):
        indent_depth = 1
        indent_str = "   |"
        level += 1
        if isinstance(element, dict):
            for key in element:
                print(f"{level*indent_depth*indent_str+key}:")
                self.print_recursive(element[key], level)
        elif isinstance(element, list):
            for i, val in enumerate(element):
                print(f"{level*indent_depth*indent_str+str(i)}:")
                self.print_recursive(val, level)
        else:
            print(f"{level*indent_depth*indent_str+element}")
            return

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_content = tomli.loads(content)
        project_info = parsed_content["tool"]["poetry"]
        project = Project(project_info["name"], project_info["description"], project_info["dependencies"], project_info["dev-dependencies"])

        # print(content)
        # print("")
        # self.print_recursive(parsed_content, 0)
        # print("")

        return project # Project("Test name", "Test description", [], [])
