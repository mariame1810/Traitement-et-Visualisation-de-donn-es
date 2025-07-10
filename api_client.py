import os
import requests
import pandas as pd
from urllib.parse import quote

class APIClient:
    def __init__(self, base_url="https://data.opendatasoft.com/api/explore/v2.1"):
        self.base_url = base_url  # URL de base de l'API

    def get_datasets(self):
        """Appelle l'API pour récupérer les données."""
        endpoint = "/catalog/datasets"  # Endpoint pour lister les datasets
        url = self.base_url + endpoint  # URL complète pour accéder à l'API

        response = requests.get(url)  # Envoie la requête GET à l'API

        if response.status_code == 200:  # Vérifie si l'appel API a réussi verifié avecpostman
            print("API appelée avec succès!")
            return response.json()  # Retourne les données au format JSON
        else:
            print("Erreur lors de l'appel API:", response.status_code)  # Affiche un message d'erreur en cas d'échec
            return None  # Retourne None si l'appel échoue

    def parse_datasets(self, api_response):
        """Extrait les noms, descriptions et métadonnées des jeux de données."""
        datasets = []  # Liste vide pour stocker les informations extraites

        for dataset in api_response['results']:  # On parcourt chaque dataset dans la réponse
            datasets.append({
                "Nom": dataset.get("dataset_id", "N/A"),  # Récupère le nom ou "N/A" si non trouvé
                "Titre": dataset.get("title", "N/A"),  # Récupère le titre ou "N/A" si non trouvé
                "Description": dataset.get("description", "N/A"),  # Idem pour la description
                "Dernière Mise à Jour": dataset.get("modified", "N/A")  # Date de dernière mise à jour
            })

        return pd.DataFrame(datasets)  # Retourne un DataFrame pandas avec les informations extraites

    def dl_dataset(self, dataset_id, output_format="json"):
        """ methode qui permet de telecharger les données pour un dataset en particulier"""

        #verification du format
        if output_format not in ["json", "csv"]:
            print("Mauvais format !")
            return


        #construction de l'url pour dl le dataset
        endpoint = f"/catalog/datasets/{dataset_id}/exports/{output_format}"
        url = self.base_url + endpoint
        print(f"Dataset ID (original): {dataset_id}")
        print(f"URL générée : {url}")

        #envoie de la requête GET
        response = requests.get(url)

        #check la requête
        if response.status_code ==200:
            print(f"Données du datasets{dataset_id} téléchargés avec succès !")

            #création du dossier data
            if not os.path.exists("data"):
                os.makedirs("data")

            #détérmination du chemin pour la sauvegarde
            file_extension = "json" if output_format == "json" else "csv"
            file_path = f"data/{dataset_id}.{file_extension}"

            #sauvegarde du fichier
            with open(file_path, "wb") as f:
                f.write(response.content)

            print(f"Données sauvegardées dans {file_path}")
        elif response.status_code == 404:
            print(f"Erreur : le dataset '{dataset_id}' n'est pas disponible au format '{output_format}'.")
        else :
            print(f"Erreur lors du téléchargement : {response.status_code}")
