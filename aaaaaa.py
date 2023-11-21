import subprocess
import json

class Repository():
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.branches = []

    def get_branches(self):
        command = ["gh", "repo", "view", "--json=branches", self.name]
        print(" ".join(command))

        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
            repo_data = json.loads(result.stdout)
            branches_data = repo_data['branches']

            for branch_data in branches_data:
                branch_name = branch_data['name']
                self.branches.append(branch_name)
        except subprocess.CalledProcessError as e:
            print(f"Erreur : {e}")

# Exemple d'utilisation avec un répertoire spécifique
repository_name = 'NomRepo1'  # Remplacez par le nom du répertoire souhaité
repository_url = 'https://github.com/proprietaire1/NomRepo1'  # Remplacez par l'URL du répertoire

repo = Repository(repository_name, repository_url)
repo.get_branches()

print("Noms des branchessssss :", repo.branches)
