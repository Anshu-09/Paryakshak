import random

def predict_risks(records):
    """Generate risk predictions based on multiple factors"""
    results = []
    for r in records:
        # Base risk calculation using available data
        base_risk = 0.3
        
        # Adjust risk based on location deviation
        if r["location"] != r["expected"]:
            base_risk += 0.4
        
        # Adjust risk based on incident flag
        if r.get("incident_flag", False):
            base_risk += 0.5
        
        # Adjust risk based on crowd level
        crowd_level = r.get("crowd_level", 50)
        if crowd_level < 10:  # Too isolated
            base_risk += 0.2
        elif crowd_level > 80:  # Overcrowded
            base_risk += 0.3
        
        # Adjust risk based on weather
        weather = r.get("weather_condition", "clear")
        if weather in ["rainy", "foggy", "stormy"]:
            base_risk += 0.2
        
        # Use existing safety score if available
        if "safety_score" in r:
            base_risk = 1 - r["safety_score"]
        
        # Add some randomness for ML simulation
        risk = min(1.0, base_risk + random.uniform(-0.1, 0.1))
        risk = round(risk, 2)
        
        # Determine status and recommendations
        if risk > 0.8:
            status = "Critical Risk"
            recommendation = "Immediate intervention required"
        elif risk > 0.6:
            status = "High Risk"
            recommendation = "Monitor closely and consider assistance"
        elif risk > 0.4:
            status = "Medium Risk"
            recommendation = "Regular monitoring advised"
        else:
            status = "Low Risk"
            recommendation = "Continue normal monitoring"
        
        results.append({
            "tourist_id": r["tourist_id"],
            "risk_score": risk,
            "status": status,
            "recommendation": recommendation,
            "location": r["location"],
            "timestamp": r.get("timestamp", ""),
            "factors": {
                "location_deviation": r["location"] != r["expected"],
                "incident_reported": r.get("incident_flag", False),
                "crowd_level": crowd_level,
                "weather_condition": weather
            }
        })
    return results
