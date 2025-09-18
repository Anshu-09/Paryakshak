from datetime import datetime

def generate_report(anomalies, predictions):
    """Generate comprehensive safety report for dashboard"""
    
    # Calculate statistics
    total_tourists = len(predictions)
    critical_risk = len([p for p in predictions if p["risk_score"] > 0.8])
    high_risk = len([p for p in predictions if p["risk_score"] > 0.6 and p["risk_score"] <= 0.8])
    medium_risk = len([p for p in predictions if p["risk_score"] > 0.4 and p["risk_score"] <= 0.6])
    low_risk = len([p for p in predictions if p["risk_score"] <= 0.4])
    
    # Anomaly breakdown
    anomaly_types = {}
    for anomaly in anomalies:
        anomaly_type = anomaly.get("type", "unknown")
        anomaly_types[anomaly_type] = anomaly_types.get(anomaly_type, 0) + 1
    
    # Average risk score
    avg_risk = round(sum(p["risk_score"] for p in predictions) / total_tourists, 2) if total_tourists > 0 else 0
    
    # Generate summary text
    summary = f"Monitoring {total_tourists} tourists. {len(anomalies)} anomalies detected. Average risk score: {avg_risk}."
    if critical_risk > 0:
        summary += f" {critical_risk} tourists require immediate attention."
    
    # Recommendations
    recommendations = []
    if critical_risk > 0:
        recommendations.append("Deploy emergency response teams to critical risk tourists")
    if high_risk > 0:
        recommendations.append(f"Increase monitoring for {high_risk} high-risk tourists")
    if "incident_reported" in anomaly_types:
        recommendations.append("Investigate reported incidents immediately")
    if "location_deviation" in anomaly_types:
        recommendations.append("Contact tourists who deviated from expected routes")
    
    report = {
        "report_id": f"RPT_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "generated_at": datetime.now().isoformat(),
        "summary": summary,
        "statistics": {
            "total_tourists": total_tourists,
            "total_anomalies": len(anomalies),
            "average_risk_score": avg_risk,
            "risk_distribution": {
                "critical_risk": critical_risk,
                "high_risk": high_risk,
                "medium_risk": medium_risk,
                "low_risk": low_risk
            },
            "anomaly_breakdown": anomaly_types
        },
        "recommendations": recommendations,
        "detailed_data": {
            "anomalies": anomalies,
            "predictions": predictions
        }
    }
    return report
