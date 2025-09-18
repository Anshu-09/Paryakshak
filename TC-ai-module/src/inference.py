import os
import joblib

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'anomaly_model.pkl')

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def predict_point(model, latitude, longitude, zone_risk):
    """
    model: scikit-learn model or None
    returns: 'anomaly' or 'normal'
    """
    if model is not None:
        try:
            pred = model.predict([[float(latitude), float(longitude), float(zone_risk)]])
            return 'anomaly' if int(pred[0]) == -1 else 'normal'
        except Exception as e:
            # fallback to rules if model fails
            pass

    # Simple rule-based fallback:
    if zone_risk == 1:
        return 'anomaly'
    return 'normal'