from scripts.generate_data import generate_mali_crop_data
from scripts.analyze_data import analyze_data
from scripts.visualize_data import visualize_data
from scripts.model import train_model

if __name__ == "__main__":
    # Générer les données
    generate_mali_crop_data()
    
    # Analyser les données
    analyze_data()
    
    # Visualiser les données
    visualize_data()
    
    # Entraîner et évaluer le modèle
    train_model()
 
