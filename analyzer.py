from patterns import RISK_PATTERNS

def analyze_policy(text):
    text_lower = text.lower()
    findings = []

    for pattern in RISK_PATTERNS:
        for keyword in pattern["keywords"]:
            if keyword in text_lower:
                findings.append({
                    "category": pattern["category"],
                    "risk_level": pattern["risk_level"],
                    "matched_keyword": keyword
                })
                break

    return findings
