# 🔍 Privacy Policy Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/CLI-Terminal-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" />
</p>

<p align="center">
  <b>A Python-based privacy analysis tool that scans privacy policies for risky data collection and sharing practices.</b>
</p>

---

## 🚨 Why This Project Exists

Most users accept privacy policies without understanding:

* what data is collected,
* who receives the data,
* whether data is sold,
* how long information is stored,
* or how invasive the platform actually is.

This tool helps identify potentially risky clauses automatically using pattern-based analysis.

---

# ✨ Features

✅ Detects risky privacy clauses
✅ Flags suspicious data practices
✅ Calculates overall risk score
✅ CLI-based fast scanning
✅ Lightweight and dependency-free
✅ Simple and beginner-friendly architecture

---

# ⚠️ Risk Categories

| Category                   | Severity  |
| -------------------------- | --------- |
| Data Selling               | 🔴 HIGH   |
| Third-Party Sharing        | 🔴 HIGH   |
| Camera / Microphone Access | 🔴 HIGH   |
| Location Tracking          | 🟡 MEDIUM |
| Behavioral Profiling       | 🟡 MEDIUM |
| Government Disclosure      | 🟡 MEDIUM |
| Data Retention Policies    | 🟢 LOW    |

---

# 🛠️ Tech Stack

| Technology    | Purpose           |
| ------------- | ----------------- |
| Python 3      | Core development  |
| Regex (`re`)  | Pattern detection |
| CLI           | User interaction  |
| File Handling | Policy processing |

---

# 📁 Project Structure

```bash
privacy-policy-analyzer/
├── main.py
├── analyzer.py
├── patterns.py
├── reporter.py
└── test_policies/
```

---

# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/UtkarshaWaghmare101/privacy-policy-analyzer.git
cd privacy-policy-analyzer
```

---

## 2️⃣ Run the Scanner

```bash
python main.py
```

---

## 3️⃣ Paste Privacy Policy Text

Paste policy content into terminal.

Type:

```text
END
```

to finish scanning.

---

# 📊 Example Output

```text
[HIGH] Data Selling
Matched: "sell your data"

[HIGH] Third Party Sharing
Matched: "share your information"

[MEDIUM] Location Tracking
Matched: "track your location"

===================================
Risk Score : 120
Verdict    : DANGEROUS
===================================
```

---

# ⚙️ How It Works

1. User pastes privacy policy text
2. Regex-based rules scan content
3. Risk patterns are matched
4. Severity score is calculated
5. Final verdict is generated

---

# 🔐 Concepts Explored

* Privacy Engineering
* Sensitive Data Analysis
* Risk Classification
* Pattern Matching
* Security Tooling
* CLI Application Design

---

# 🚀 Future Improvements

* AI-powered semantic analysis
* PDF privacy policy support
* Web dashboard interface
* Risk visualization charts
* Browser extension integration
* False-positive reduction

---

# 🌐 Inspiration

Inspired by modern privacy engineering and security analysis workflows used in real-world developer tooling.

---

# 📄 License

This project is licensed under the MIT License.
