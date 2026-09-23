import pytest
from src.logsentinel.analyzer import PayloadAnalyzer

def test_analyzer_detects_clean_request():
    analyzer = PayloadAnalyzer()
    assert analyzer.scan_request("/index.html") == "Clean"
    assert analyzer.scan_request("/about-us?lang=en") == "Clean"

def test_analyzer_detects_sqli():
    analyzer = PayloadAnalyzer()
    assert analyzer.scan_request("/login?user=' OR 1=1--") == "SQLi Attempt"
    assert analyzer.scan_request("/search?q=admin' --") == "SQLi Attempt"
    assert analyzer.scan_request("/drop_table?query=DROP TABLE users;") == "SQLi Attempt"

def test_analyzer_detects_xss():
    analyzer = PayloadAnalyzer()
    assert analyzer.scan_request("/search?q=<script>alert(1)</script>") == "XSS Attempt"
    assert analyzer.scan_request("/profile?name=<img src=x onerror=alert(1)>") == "XSS Attempt"