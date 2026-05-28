from analyzer import analyze_policy
from reporter import print_report, save_report

def calculate_risk_score(findings):
    score = 0
    for finding in findings:
        if finding["risk_level"] == "HIGH":
            score += 30
        elif finding["risk_level"] == "MEDIUM":
            score += 15
        elif finding["risk_level"] == "LOW":
            score += 5

    if score >= 60:
        verdict = "DANGEROUS - Avoid this service"
    elif score >= 30:
        verdict = "RISKY - Read carefully before agreeing"
    else:
        verdict = "MODERATE - Some risks present"

    return score, verdict

def main():
    print("=== Privacy Policy Analyzer ===")
    print("Paste privacy policy text below.")
    print("Type END on a new line when done.")
    print()

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    policy_text = "\n".join(lines)
    findings = analyze_policy(policy_text)
    score, verdict = calculate_risk_score(findings)
    print_report(findings, score, verdict)
    save_report(findings, score, verdict)

main()
