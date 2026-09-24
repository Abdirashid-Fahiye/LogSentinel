import os
import requests

class ThreatIntelAPI:
    def __init__(self, api_key: str = None):
        # Allow passing an API key directly or reading from environment variables
        self.api_key = api_key or os.getenv("ABUSEIPDB_API_KEY", "")
        self.base_url = "https://api.abuseipdb.com/api/v2/check"

    def check_ip(self, ip_address: str) -> dict:
        """Queries the AbuseIPDB API for threat intelligence scoring."""
        headers = {
            "Accept": "application/json",
            "Key": self.api_key
        }
        params = {
            "ipAddress": ip_address,
            "maxAgeInDays": "90"
        }
        
        try:
            response = requests.get(self.base_url, headers=headers, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json().get("data", {})
                return {
                    "ipAddress": data.get("ipAddress", ip_address),
                    "abuseConfidenceScore": data.get("abuseConfidenceScore", 0)
                }
            return {"ipAddress": ip_address, "abuseConfidenceScore": 0, "error": f"Status {response.status_code}"}
        except requests.exceptions.RequestException as e:
            return {"ipAddress": ip_address, "abuseConfidenceScore": 0, "error": str(e)}