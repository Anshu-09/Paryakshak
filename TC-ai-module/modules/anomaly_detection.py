def detect_anomalies(records):
    """Detect anomalies in tourist behavior and safety"""
    anomalies = []
    for r in records:
        # Location deviation
        if r["location"] != r["expected"]:
            anomalies.append({
                "tourist_id": r["tourist_id"],
                "type": "location_deviation",
                "severity": "high" if "restricted" in r["location"].lower() else "medium",
                "description": "Tourist deviated from expected route",
                "current_location": r["location"],
                "expected_location": r["expected"],
                "timestamp": r.get("timestamp", "")
            })
        
        # Incident flag anomaly
        if r.get("incident_flag", False):
            anomalies.append({
                "tourist_id": r["tourist_id"],
                "type": "incident_reported",
                "severity": "critical",
                "description": "Incident reported at location",
                "location": r["location"],
                "timestamp": r.get("timestamp", "")
            })
        
        # Low safety score anomaly
        if r.get("safety_score", 1.0) < 0.4:
            anomalies.append({
                "tourist_id": r["tourist_id"],
                "type": "low_safety_score",
                "severity": "high",
                "description": f"Low safety score detected: {r.get('safety_score', 0)}",
                "location": r["location"],
                "safety_score": r.get("safety_score", 0),
                "timestamp": r.get("timestamp", "")
            })
    
    return anomalies
