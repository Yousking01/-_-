import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(filename='data/mali_crop_data.csv'):
    """Entraîne un modèle pour prédire les cultures."""
    crop_df = pd.read_csv(filename)
    
    # Préparer les données
    X = crop_df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = crop_df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Entraîner le modèle
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Évaluer le modèle
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
 
