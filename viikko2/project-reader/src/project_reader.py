from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("Merkkijonomuotoinen sisältö:\n", content)

        toml_dictionary = toml.loads(content)["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        print("TOML-formaatissa oleva sisältö:")
        return Project(toml_dictionary["name"], 
        toml_dictionary["description"], 
        toml_dictionary["dependencies"], 
        toml_dictionary["dev-dependencies"])
