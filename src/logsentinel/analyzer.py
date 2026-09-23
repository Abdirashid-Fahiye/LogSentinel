import re

class PayloadAnalyzer:
    def __init__(self):
        # Regex for SQLi: Looks for ' OR, -- (SQL comments), and DROP TABLE commands
        self.sqli_pattern = re.compile(
            r"(?i)(?:'|%27)\s*(?:OR|AND)|(?:--)|DROP\s+TABLE"
        )
        
        # Regex for XSS: Looks for <script> tags and onerror= attributes
        self.xss_pattern = re.compile(
            r"(?i)(?:<|%3C)script|onerror="
        )

    def scan_request(self, request: str) -> str:
        """Scans an HTTP request URL for known malicious payloads."""
        if self.xss_pattern.search(request):
            return "XSS Attempt"
        
        if self.sqli_pattern.search(request):
            return "SQLi Attempt"
        
        return "Clean"