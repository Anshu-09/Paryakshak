import os
import joblib
from sklearn.ensemble import IsolationForest
from preprocessing import generate_sample_csv, load_csv, feature_engineer

MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models'))
MODEL_PATH = os.path.join(MODEL_DIR, 'anomaly_model.pkl')
DATA_PATH = os.path.join(MODEL_DIR, 'tourist_data.csv')

def train_and_save(data_path=DATA_PATH, model_path=MODEL_PATH):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    generate_sample_csv(data_path, n=500)
    df = load_csv(data_path)
    X = feature_engineer(df)
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(X)
    joblib.dump(model, model_path)
    print("Model trained and saved to:", model_path)

if __name__ == '__main__':
    train_and_save()
