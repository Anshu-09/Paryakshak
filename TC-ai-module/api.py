from fastapi import FastAPI
from modules.preprocess import load_dummy_data, clean_data
from modules.anomaly_detection import detect_anomalies
from modules.prediction import predict_risks
from modules.report_generator import generate_report

app = FastAPI(title="Paryakshak AI Module", description="AI + Dashboard backend helper for tourist safety monitoring")

@app.get("/")
def root():
    return {"message": "Paryakshak AI Module is running", "status": "active", "version": "1.0.0"}

@app.get("/preprocess")
def preprocess():
    """Load and preprocess dummy data"""
    raw_data = load_dummy_data()
    cleaned_data = clean_data(raw_data)
    return {"raw_count": len(raw_data), "cleaned_count": len(cleaned_data), "data": cleaned_data}

@app.get("/detect-anomalies")
def detect_anomalies_endpoint():
    """Detect anomalies in tourist behavior"""
    data = clean_data(load_dummy_data())
    anomalies = detect_anomalies(data)
    return {"anomalies_detected": len(anomalies), "anomalies": anomalies}

@app.get("/predict")
def predict():
    """Generate risk predictions for tourists"""
    data = clean_data(load_dummy_data())
    predictions = predict_risks(data)
    return {"predictions_count": len(predictions), "predictions": predictions}

@app.get("/generate-report")
def generate_report_endpoint():
    """Generate comprehensive safety report"""
    data = clean_data(load_dummy_data())
    anomalies = detect_anomalies(data)
    predictions = predict_risks(data)
    report = generate_report(anomalies, predictions)
    return report

# Legacy endpoints for backward compatibility
@app.get("/anomalies")
def anomalies():
    data = clean_data(load_dummy_data())
    return detect_anomalies(data)

@app.get("/predictions")
def predictions():
    data = clean_data(load_dummy_data())
    return predict_risks(data)

@app.get("/report")
def report():
    data = clean_data(load_dummy_data())
    anomalies = detect_anomalies(data)
    predictions = predict_risks(data)
    return generate_report(anomalies, predictions)
