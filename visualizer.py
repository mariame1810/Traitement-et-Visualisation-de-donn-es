import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def plot_bar(self, data, column, title, xlabel, ylabel):
        """Affiche un graphique à barres pour une colonne donnée."""
        data[column].value_counts().plot(kind='bar')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_heatmap(self, data, x_col, y_col, title):
        """Affiche une heatmap de la densité géographique"""
        plt.figure(figsize=(10, 6))
        sns.kdeplot(
            x=data[x_col],
            y=data[y_col],
            fill=True,
            cmap='Reds',
            alpha=0.6,
            levels=100
        )
        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.tight_layout()
        plt.show()


    def plot_scatter(self, data, x_col, y_col, title, xlabel, ylabel):
        """Affiche un nuage de points pour deux colonnes numériques."""
        plt.scatter(data[x_col], data[y_col], alpha=0.6)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.show()

    def plot_histogram(self, data, column, bins, title, xlabel, ylabel):
        """Affiche un histogramme pour une colonne numérique."""
        data[column].plot(kind='hist', bins=bins, alpha=0.7)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tight_layout()
        plt.show()
