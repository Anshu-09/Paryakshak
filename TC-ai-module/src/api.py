# AI Module entry
from fastapi import FastAPI
from pydantic import BaseModel
from inference import load_model, predict_point

app = FastAPI(title="Paryakshak AI Module")

class LocationInput(BaseModel):
    latitude: float
    longitude: float
    zone_risk: int = 0

MODEL = None

@app.on_event("startup")
def startup_event():
    global MODEL
    MODEL = load_model()

@app.get("/")
def root():
    return {"message": "Paryakshak AI module is running"}

@app.post("/predict")
def predict(input: LocationInput):
    status = predict_point(MODEL, input.latitude, input.longitude, input.zone_risk)
    return {"status": status}
