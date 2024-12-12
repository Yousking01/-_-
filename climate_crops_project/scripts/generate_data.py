import pandas as pd
import numpy as np

def generate_mali_crop_data(filename='data/mali_crop_data.csv', n=1000):
    """Génère un dataset synthétique pour les cultures au Mali."""
    data = {
        'N': np.random.randint(10, 100, n),
        'P': np.random.randint(5, 50, n),
        'K': np.random.randint(5, 60, n),
        'temperature': np.random.uniform(20, 40, n),
        'humidity': np.random.uniform(15, 70, n),
        'ph': np.random.uniform(5.5, 7.5, n),
        'rainfall': np.random.uniform(50, 250, n),
        'label': np.random.choice(['papaya', 'orange'], n)
    }
    crop_df = pd.DataFrame(data)
    crop_df.to_csv(filename, index=False)
    print(f"Dataset saved to {filename}")

