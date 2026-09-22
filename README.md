# LogSentinel: Automated Threat Intelligence & Log Auditing CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Security](https://img.shields.io/badge/Security-SIEM%20%7C%20Threat%20Intel-red) ![Testing](https://img.shields.io/badge/Testing-PyTest%20%7C%20TDD-brightgreen)

A Python-based defensive cybersecurity tool designed to ingest web server access logs, detect OWASP Top 10 malicious payloads, and cross-reference attacker IP addresses against global Threat Intelligence APIs.

## 🛑 The Problem: Manual Log Auditing
Web servers generate thousands of log entries daily. When a security breach occurs, analysts are forced to manually comb through raw `.log` text files to identify the attacker's IP address and the specific vulnerability they exploited. This manual process is slow and prone to human error, allowing threats to persist unnoticed.

## 💡 The Solution: Automated Triage
LogSentinel automates the initial triage process for Security Operations Centers (SOCs). It acts as a lightweight SIEM (Security Information and Event Management) tool that:
1. **Parses** raw Nginx/Apache logs into structured data.
2. **Analyzes** HTTP request payloads for static Indicators of Compromise (IoCs), such as SQL Injection (SQLi) and Cross-Site Scripting (XSS).
3. **Enriches** the data by asynchronously calling the AbuseIPDB API to determine if the extracted IP addresses belong to known botnets or malicious actors.

## 🏗️ Architecture Layout

```text
LogSentinel/
├── src/logsentinel/
│   ├── __init__.py
│   ├── parser.py        # Regex-based log ingestion and normalization
│   ├── analyzer.py      # Static intrusion detection (SQLi/XSS pattern matching)
│   ├── threat_intel.py  # Asynchronous REST API integration (AbuseIPDB)
│   └── reporter.py      # Aggregates results into JSON/Terminal output
├── tests/
│   └── test_parser.py   # PyTest unit tests for TDD
├── requirements.txt
└── README.md



⚙️ How to Run Locally
Prerequisites
Python 3.10+

An active API key from AbuseIPDB

Installation & Execution
Bash
# Clone the repository
git clone [https://github.com/Abdirashid-Fahiye/LogSentinel.git](https://github.com/Abdirashid-Fahiye/LogSentinel.git)
cd LogSentinel

# Activate virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the test suite
pytest tests/


👤 Technical Author
Developer: Abdirashid Fahiye

Programme: WeThinkCode_ Software Engineering (Cybersecurity Elective Project)

🔒 WeThinkCode_ Verification
Verification Code: