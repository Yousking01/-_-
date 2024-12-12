import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(filename='data/mali_crop_data.csv'):
    """Visualisations des données."""
    crop_df = pd.read_csv(filename)
    
    # Répartition des cultures
    sns.countplot(data=crop_df, x='label')
    plt.title("Répartition des cultures")
    plt.show()
    
    # Corrélation entre les variables
    sns.heatmap(crop_df.corr(), annot=True, cmap='coolwarm')
    plt.title("Corrélation entre les variables")
    plt.show()
 
