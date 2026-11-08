from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # luetaan tiedosta ja palautetaan Project-olio
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomllib.loads(content) 
        project_data = data["project"]

        name = project_data["name"]
        description = project_data.get("description", "")
        license = project_data.get("license", "-")
        if isinstance(license, dict):
            license = license.get("text", "-")
        authors = [
            author.get("name", "") if isinstance(author, dict) else author
            for author in project_data.get("authors", [])
        ]
        dependencies = project_data.get("dependencies", [])
        dev_dependencies = data.get("dependency-groups", {}).get("dev", [])


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            name, description, dependencies, dev_dependencies, license, authors
        )
