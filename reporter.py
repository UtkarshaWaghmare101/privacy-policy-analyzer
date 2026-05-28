import json

def print_report(findings, score, verdict):
    print("\n" + "="*40)
    print("       PRIVACY POLICY SCAN REPORT")
    print("="*40)

    if not findings:
        print("No risks detected.")
    else:
        for f in findings:
            print(f"[{f['risk_level']}] {f['category']}")
            print(f"     Matched: '{f['matched_keyword']}'")
            print()

    print(f"Risk Score : {score}")
    print(f"Verdict    : {verdict}")
    print("="*40)

def save_report(findings, score, verdict):
    report = {
        "total_risks_found": len(findings),
        "risk_score": score,
        "verdict": verdict,
        "findings": findings
    }
    with open("privacy_report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("\nReport saved to privacy_report.json")
