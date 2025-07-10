import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, filepath):
        self.file_path= filepath

    def load_data(self):
        """Charge les données dans un DataFrame"""

        try:
            data=pd.read_csv(self.file_path, delimiter=';', on_bad_lines="skip", encoding='utf-8')
            print("Données téléchargées ")
            return data
        except Exception as e:
            print(f"Erreur lors du dl {e}")
            return None

    def clean_data(self, data):
        """Nettoyage"""

        #Renommer les colonnes
        data.columns = data.columns.str.strip().str.replace(' ', '_').str.lower()

        #Suppression de colonne inutile
        if 'geo_shape' in data.columns:
            data = data.drop(['geo_shape'], axis=1)

        #Suppression des doublons
        data = data.drop_duplicates()

        #Suppression des colonnes avec data manquantes
        data=data.dropna(axis=1, thresh=len(data) *0.5)

        #Remplissage des données manquantes qui restent
        data = data.fillna({'iso_3_country_code': 'Inconnu', 'english_name': 'Inconnu'})

        #Extraction des coordonnées depuis geo_point
        if 'geo_point' in data.columns:
            data['latitude'] = data['geo_point'].apply(lambda x: float(x.split(',')[0]) if isinstance(x, str) else None)
            data['longitude'] = data['geo_point'].apply(lambda x: float(x.split(',')[1]) if isinstance(x, str) else None)
            data = data.drop(['geo_point'], axis=1)  # Supprime Geo Point si inutile

        print("Données nettoyées")
        return data

    def dataset_infos(self, data):
        """Affiche des informations générales sur le dataset."""
        print("----- Résumé du Dataset -----")
        print(f"Nombre de lignes : {data.shape[0]}")
        print(f"Nombre de colonnes : {data.shape[1]}")
        print("\n--- Types de données :")
        print(data.dtypes)
        print("\n--- Aperçu des données manquantes :")
        print(data.isnull().sum())
        print("\n--- Exemple des premières lignes :")
        print(data.head())
        print("--------------------------------")

    def detect_outliers(self, data, column):
        """Detecte les valeurs aberrantes dans une colonne"""
        q1 = data[column].quantile(0.25)
        q3 = data[column].quantile(0.75)
        iqr= q3-q1
        low = q1 - 1.5 * iqr
        up = q3 + 1.5 * iqr
        return data[(data[column] < low) | (data[column] > up)]

    def normalize_data(self, data):
        """Normalisation des colonnes"""
        for column in data.select_dtypes(include=[np.number]):
            data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
        print("Données normalisées.")
        return data
