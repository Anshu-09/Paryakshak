# TC-ai-module

**AI + Dashboard Backend Helper for Paryakshak System**

This module provides AI-powered tourist safety monitoring capabilities for the Paryakshak project (SIH 2025). It exposes REST APIs that can be consumed by the dashboard to analyze tourist behavior, detect anomalies, predict risks, and generate comprehensive safety reports.

## Features

- **Real-time Anomaly Detection**: Identifies unusual tourist behavior patterns
- **Risk Prediction**: ML-based risk scoring for tourist safety
- **Data Preprocessing**: Cleans and normalizes tourist data
- **Report Generation**: Comprehensive safety reports with actionable insights
- **RESTful APIs**: Easy integration with dashboard and other services

## Project Structure

```
TC-ai-module/
│
├── api.py                     # FastAPI entry point with all endpoints
│
├── modules/                   # AI submodules
│   ├── __init__.py
│   ├── preprocess.py          # Data loading & cleaning
│   ├── anomaly_detection.py   # Anomaly detection algorithms
│   ├── prediction.py          # Risk prediction models
│   ├── report_generator.py    # Report generation utilities
│   └── utils.py               # Helper utilities
│
├── data/                      
│   └── dummy_data.json        # Mock tourist safety data
│
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone and navigate to the module**:
   ```bash
   cd TC-ai-module
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - **Windows**: `venv\Scripts\activate`
   - **Linux/Mac**: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   python -m pip install -r requirements.txt
   ```

5. **Run the server**:
   ```bash
   python -m uvicorn api:app --reload
   ```

6. **Access the API**:
   - Server: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - OpenAPI schema: http://localhost:8000/openapi.json

## API Endpoints

### Core Endpoints

- **GET /** - Health check and module status
- **GET /preprocess** - Load and preprocess tourist data
- **GET /detect-anomalies** - Detect anomalies in tourist behavior
- **GET /predict** - Generate risk predictions for tourists
- **GET /generate-report** - Create comprehensive safety reports

### Legacy Endpoints (Backward Compatibility)

- **GET /anomalies** - Simple anomaly detection
- **GET /predictions** - Basic risk predictions
- **GET /report** - Basic report generation

## API Response Examples

### Anomaly Detection Response
```json
{
  "anomalies_detected": 3,
  "anomalies": [
    {
      "tourist_id": "T002",
      "type": "location_deviation",
      "severity": "medium",
      "description": "Tourist deviated from expected route",
      "current_location": "Unknown Trail",
      "expected_location": "Elephant Falls",
      "timestamp": "2024-01-15T11:15:00Z"
    }
  ]
}
```

### Risk Prediction Response
```json
{
  "predictions_count": 5,
  "predictions": [
    {
      "tourist_id": "T001",
      "risk_score": 0.23,
      "status": "Low Risk",
      "recommendation": "Continue normal monitoring",
      "location": "Shillong Peak",
      "factors": {
        "location_deviation": false,
        "incident_reported": false,
        "crowd_level": 45,
        "weather_condition": "clear"
      }
    }
  ]
}
```

## Current Implementation Status

### ✅ Completed Features
- FastAPI server with all required endpoints
- Dummy data simulation with realistic tourist scenarios
- Multi-factor anomaly detection (location, incidents, safety scores)
- Risk prediction based on multiple parameters
- Comprehensive report generation with statistics and recommendations
- Proper error handling and response formatting

### 🔄 Using Dummy Data
Currently using mock data for development. The following components use placeholder implementations:
- **Data Source**: Local JSON file instead of real backend APIs
- **ML Models**: Rule-based algorithms instead of trained models
- **External APIs**: Simulated responses for weather, crowd data, etc.

### 🚀 Future Integration Points
- Replace `load_dummy_data()` with real backend API calls
- Integrate actual ML models for risk prediction
- Connect to real-time data sources (GPS, IoT sensors, weather APIs)
- Add authentication and authorization
- Implement data persistence and caching

## Development Notes

### Adding New Endpoints
1. Define the endpoint in `api.py`
2. Implement business logic in appropriate module under `modules/`
3. Update this README with endpoint documentation

### Replacing Dummy Data
1. Update `modules/preprocess.py` to call real APIs
2. Modify `modules/utils.py` for production data handling
3. Update data models in respective modules

### Testing the APIs
Use the interactive documentation at http://localhost:8000/docs or test with curl:

```bash
# Test anomaly detection
curl http://localhost:8000/detect-anomalies

# Test risk prediction
curl http://localhost:8000/predict

# Generate report
curl http://localhost:8000/generate-report
```

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **Pydantic**: Data validation and serialization
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning library (for future ML models)
- **NumPy**: Numerical computing
- **Requests**: HTTP library for API calls

## Contributing

1. Follow the existing code structure and naming conventions
2. Add proper docstrings to all functions
3. Update this README when adding new features
4. Test all endpoints before committing changes

## License

Part of the Paryakshak project for SIH 2025.