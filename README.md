# LogSentinel: Automated Threat Intelligence & Log Auditing CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Security](https://img.shields.io/badge/Security-SIEM%20%7C%20Threat%20Intel-red) ![Testing](https://img.shields.io/badge/Testing-PyTest%20%7C%20TDD-brightgreen)

A Python-based defensive cybersecurity Command Line Interface (CLI) designed to ingest web server access logs, detect OWASP Top 10 malicious payloads, and cross-reference attacker IP addresses against global Threat Intelligence APIs.

## 🛑 The Problem: Manual Log Auditing
Web servers generate thousands of raw text log entries daily. When a security breach occurs, analysts are forced to manually comb through `.log` files to identify the attacker's IP address and the specific vulnerability they exploited. This manual triage process is slow, inefficient, and highly prone to human error, allowing threats to persist unnoticed.



## 💡 The Solution: Automated Triage
LogSentinel automates the initial triage process for Security Operations Centers (SOCs). It acts as a lightweight SIEM (Security Information and Event Management) tool that implements three core defensive cybersecurity pillars:
1. **Ingestion:** Parses raw, unstructured Nginx/Apache logs into structured, searchable dictionaries.
2. **Static Intrusion Detection:** Analyzes HTTP request payloads for static Indicators of Compromise (IoCs), specifically identifying SQL Injection (SQLi) and Cross-Site Scripting (XSS) attacks.
3. **Threat Intelligence Enrichment:** Asynchronously queries the AbuseIPDB API to determine if the extracted IP addresses belong to known botnets or malicious actors.




## 🏗️ Architecture & Modules

```text
LogSentinel/
├── src/logsentinel/
│   ├── __init__.py      # Designates the directory as a Python package.
│   ├── __main__.py      # The CLI entry point. Executes the Reporter when the module is run.
│   ├── parser.py        # Contains LogParser. Uses Regex to extract IPs and URLs from raw text.
│   ├── analyzer.py      # Contains PayloadAnalyzer. Uses Regex to flag SQLi/XSS patterns.
│   ├── threat_intel.py  # Contains ThreatIntelAPI. Handles HTTP requests to the AbuseIPDB REST API.
│   └── reporter.py      # Contains Reporter. Orchestrates the pipeline and formats the terminal output.
├── tests/
│   ├── test_analyzer.py # TDD suite proving accurate SQLi/XSS detection.
│   ├── test_parser.py   # TDD suite proving regex extraction and fault tolerance.
│   └── test_threat_intel.py # TDD suite using mock API calls to prevent live network testing.
├── requirements.txt
└── README.md



⚙️ How to Run Locally

Prerequisites
Python 3.10+

An active API key from AbuseIPDB

Installation
Bash
# Clone the repository
git clone [https://github.com/Abdirashid-Fahiye/LogSentinel.git](https://github.com/Abdirashid-Fahiye/LogSentinel.git)
cd LogSentinel

# Activate virtual environment and install dependencies (Linux/macOS)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Running the Test Suite
This project was built using strict Test-Driven Development (TDD). To verify the mathematical contracts of the security rules:

Bash
pytest tests/
Executing the CLI
To run LogSentinel against a log file, use the module execution flag (-m):

Bash
python -m src.logsentinel tests/mock_access.log
Command Breakdown:

python: Invokes the Python interpreter.

-m src.logsentinel: The module flag (-m) tells Python to execute the src.logsentinel directory as a self-contained application by looking for the __main__.py file. This ensures all internal imports resolve correctly.

tests/mock_access.log: The argument passed to the CLI containing the target log data.

Output:
The command outputs a consolidated Audit Report Table to the terminal. It acts as a "Single Pane of Glass" for the security analyst, listing every extracted IP, its global threat score, the payload classification (Clean, SQLi Attempt, XSS Attempt), and the exact URL requested.

👤 Technical Author
Developer: Abdirashid Fahiye

Programme: WeThinkCode_ Software Engineering (Cybersecurity Elective Project)

🔒 WeThinkCode_ Verification
Verification Code: