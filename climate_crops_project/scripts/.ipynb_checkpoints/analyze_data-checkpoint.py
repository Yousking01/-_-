import pandas as pd

def analyze_data(filename='data/mali_crop_data.csv'):
    """Analyse exploratoire des données."""
    crop_df = pd.read_csv(filename)
    print("Aperçu des données :")
    print(crop_df.head())
    
    print("\nRésumé statistique :")
    print(crop_df.describe())
    
    print("\nRépartition des cultures :")
    print(crop_df['label'].value_counts())
 
