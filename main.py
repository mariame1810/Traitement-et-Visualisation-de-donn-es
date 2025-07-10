from api_client import APIClient  # Importer la classe APIClient
from dataprocessor import DataProcessor
from visualizer import Visualizer

def main():
    # Créer une instance de la classe APIClient
    #api_client = APIClient()

    # ID du dataset sélectionné
    #dataset_id = "world-administrative-boundaries"  # Remplacer par l'ID du dataset
    #output_format = "csv"  # Format souhaité pour les données (json ou csv)

    # Téléchargement des données
    #print(f"Téléchargement du dataset : {dataset_id}")
    #api_client.dl_dataset(dataset_id, output_format)

    #print(f"Le dataset '{dataset_id}' a été téléchargé avec succès.")


    file_path = "/Users/mariame/Desktop/ESGI/DATAMINING/TP/TP3rendu/data/world-administrative-boundaries.csv"
    processor = DataProcessor(file_path)

    #Charger les données
    data = processor.load_data()
    if data is None or data.empty:
        print("Erreur")
        return

    print("Aperçu/résumé des datas :")
    processor.dataset_infos(data)


    # Nettoyer les données
    cleaned_data = processor.clean_data(data)

    #Visualisation
    visualizer = Visualizer()
    #1. Graphiques en barres du nombre de territoires par continets
    visualizer.plot_bar(
        cleaned_data,
        column='continent_of_the_territory',
        title='Nombre de territoires par continent',
        xlabel='Continent',
        ylabel='Nombre de territoires'
    )

    # 2. Nuage de points de la répartition géographique
    visualizer.plot_scatter(
        cleaned_data,
        x_col='longitude',
        y_col='latitude',
        title='Répartition géographique des territoires',
        xlabel='Longitude',
        ylabel='Latitude'
    )

    # 3. Heatmap de la densité géographoque des territoires
    visualizer.plot_heatmap(
        data = cleaned_data,
        x_col='longitude',
        y_col='latitude',
        title='Densité géographique des territoires'
    )
    #4 Histogramme : distribution des codes ISO
    visualizer.plot_histogram(
    cleaned_data,
    column = 'iso_3_country_code',
    bins = 20,
    title = 'Distribution des codes ISO',
    xlabel= 'Codes ISO',
    ylabel = 'Fréquence'
    )


if __name__ == "__main__":
    main()
