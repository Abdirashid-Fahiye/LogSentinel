import json
from src.logsentinel.parser import LogParser
from src.logsentinel.analyzer import PayloadAnalyzer
from src.logsentinel.threat_intel import ThreatIntelAPI

class Reporter:
    def __init__(self, log_filepath: str, api_key: str = None):
        self.parser = LogParser(log_filepath)
        self.analyzer = PayloadAnalyzer()
        self.intel = ThreatIntelAPI(api_key=api_key)

    def generate_report(self) -> list:
        """Parses the log, analyzes payloads, enriches with threat intel, and returns findings."""
        raw_events = self.parser.parse_file()
        findings = []
        
        # Cache IP queries to prevent hitting rate limits on duplicate IPs
        ip_cache = {}

        for event in raw_events:
            ip = event['ip']
            url = event['url']
            payload_status = self.analyzer.scan_request(url)

            if ip not in ip_cache:
                ip_cache[ip] = self.intel.check_ip(ip)

            threat_info = ip_cache[ip]

            findings.append({
                "timestamp": event['timestamp'],
                "ip": ip,
                "method": event['method'],
                "url": url,
                "payload_status": payload_status,
                "threat_score": threat_info.get("abuseConfidenceScore", 0)
            })

        return findings

    def print_terminal_summary(self):
        findings = self.generate_report()
        print("\n" + "="*80)
        print(f" LOGSENTINEL AUDIT REPORT - Total Events Analyzed: {len(findings)}")
        print("="*80)
        
        for item in findings:
            alert = "[ALERT]" if item['payload_status'] != "Clean" or item['threat_score'] > 50 else "[INFO]"
            print(f"{alert} IP: {item['ip']:<15} | Threat Score: {item['threat_score']:>3}% | Payload: {item['payload_status']:<12} | URL: {item['url']}")
        print("="*80 + "\n")