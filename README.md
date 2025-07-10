# 🌍 Traitement et Visualisation de Données Géographiques

Ce projet Python vise à **extraire, nettoyer, analyser et visualiser** des données géographiques issues de jeux de données publics. Il s’appuie sur une architecture modulaire orientée objet, permettant de manipuler des fichiers CSV ou des données issues d’une API.

---

## 📂 Contenu du projet

```
.
├── api_client.py         # (optionnel) Client pour récupérer les jeux de données en ligne
├── dataprocessor.py      # Module de traitement et nettoyage des données CSV
├── visualizer.py         # Outils de visualisation : barres, heatmap, scatter, histogramme
├── main.py               # Script principal pour exécuter tout le processus
├── /data/
│   └── world-administrative-boundaries.csv  # Jeu de données géographiques utilisé
├── README.md             # Ce fichier
```

---

## 📊 Objectifs du projet

- Charger et prévisualiser des données géographiques
- Nettoyer les données : suppression des colonnes inutiles, gestion des valeurs manquantes, conversion de types
- Visualiser les données de manière claire et esthétique :  
  - par continent  
  - par répartition géographique  
  - par codes ISO

---

## ⚙️ Prérequis

- Python ≥ 3.8
- Modules :
  - `pandas`
  - `matplotlib`
  - `seaborn`

> Installez-les avec :
```bash
pip install pandas matplotlib seaborn
```

---

## 🚀 Exécution

Dans le terminal, à la racine du projet :

```bash
python main.py
```

Le script :
1. Charge les données depuis `/data/world-administrative-boundaries.csv`
2. Affiche un aperçu et les infos du dataset
3. Nettoie les données avec `DataProcessor`
4. Génère automatiquement plusieurs visualisations avec `Visualizer`

---

## 📡 Source des données

Le fichier CSV utilisé provient d’un jeu de données public sur les **limites administratives mondiales**.  
Il contient les noms de pays, codes ISO, continents, et coordonnées géographiques.

---

## 📦 Option API (facultative)

Le fichier `api_client.py` permet de récupérer dynamiquement des jeux de données via l'API d’Opendatasoft.  
Il peut être activé dans `main.py` pour remplacer les données locales par des données en ligne.

---

## ✍️ Auteur

- **Mariame Coulibaly** – [GitHub @mariame1810](https://github.com/mariame1810)

---

## 📁 Licence

Ce projet est open source, utilisable à des fins pédagogiques.
