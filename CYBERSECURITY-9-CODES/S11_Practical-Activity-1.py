# Simple Cyber Risk Assessment Simulator
def assess_risk(likelihood, impact):
    score = likelihood * impact

    if score < 4:
        severity = "Low"
    elif 4 <= score < 9:
        severity = "Medium"
    else:
        severity = "High"
    return score, severity


# Sample scenario: Phishing risk
threat_scenarios = {
    "Phishing": (3, 3),
    "Ransomware": (4, 4),
    "Data Leak": (2, 5)
}


for threat, (likelihood, impact) in threat_scenarios.items():
    score, level = assess_risk(likelihood, impact)

    print(f"{threat} ➤ Risk Score: {score} | Severity: {level}")