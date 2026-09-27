def build_alert(zone, relocation, hazard_score, overload_pct, safe_distance_km):
    if relocation == "IMMEDIATE":
        return (
            f"IMMEDIATE RELOCATION ALERT: {zone} hazard zone detected. "
            f"Hazard score {hazard_score}/100 and carrying-capacity overload "
            f"{overload_pct}%. Initiate local emergency verification, "
            f"evacuation coordination, and movement toward an approved safe "
            f"location within approximately {safe_distance_km} km, subject to "
            f"official emergency-management instructions."
        )

    if relocation == "PRIORITY":
        return (
            f"PRIORITY ALERT: {zone} risk conditions detected. "
            f"Review occupancy, hazard exposure, available capacity, and "
            f"relocation options. Current capacity overload is {overload_pct}%."
        )

    return (
        f"MONITOR ALERT: Current assessment is {zone}. "
        f"Continue monitoring hazard indicators and habitation capacity."
    )
