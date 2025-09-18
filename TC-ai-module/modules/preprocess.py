import json
import os
import requests

def load_dummy_data():
    """Load data from local dummy JSON file"""
    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "dummy_data.json")
    with open(file_path, "r") as f:
        return json.load(f)

# 🔹 Placeholder for real API integration (uncomment when backend ready)
# def load_data_from_backend():
#     response = requests.get("http://localhost:5000/api/tourists")
#     return response.json()

def clean_data(records):
    """Simple cleaning - drop records without location"""
    return [r for r in records if r.get("location")]
