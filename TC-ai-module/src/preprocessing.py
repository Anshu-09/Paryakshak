import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_sample_csv(path='../models/tourist_data.csv', n=200):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        return path
    rng = np.random.default_rng(42)
    base_lat, base_lon = 26.5, 92.9
    rows = []
    start = datetime.utcnow()
    for i in range(n):
        rows.append({
            "tourist_id": 1,
            "timestamp": (start + timedelta(minutes=5*i)).isoformat(),
            "latitude": float(base_lat + rng.normal(0, 0.005)),
            "longitude": float(base_lon + rng.normal(0, 0.005)),
            "zone_risk": int(rng.choice([0,0,0,1]))  # mostly safe
        })
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    return path

def load_csv(path='../models/tourist_data.csv'):
    return pd.read_csv(path)

def feature_engineer(df):
    # return numeric features for the simple model
    return df[['latitude', 'longitude', 'zone_risk']].astype(float)