def assess_risk(likelihood, impact):
    score = likelihood * impact

    if score < 4:
        severity = "Low"
        action = "Monitor and review quarterly."

    elif 4 <= score < 9:
        severity = "Medium"
        action = "Implement controls and review monthly."

    else:
        severity = "High"
        action = "Urgent mitigation required. Escalate to management."

    return score, severity, action


# Threats
threat_scenarios = {
    "Phishing": (3, 3),
    "Ransomware": (4, 4),
    "Insider Threat": (2, 4),
    "Supply Chain Attack": (5, 5)
}


for threat, (likelihood, impact) in threat_scenarios.items():
    score, level, response = assess_risk(likelihood, impact)
    print(f"{threat} ➤ Risk Score: {score} | Severity: {level} | Action: {response}")