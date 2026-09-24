import pytest
from unittest.mock import patch
from src.logsentinel.threat_intel import ThreatIntelAPI

@patch('src.logsentinel.threat_intel.requests.get')
def test_check_ip_malicious(mock_get):
    # Arrange: Fake a response from the AbuseIPDB API showing a 100% threat score
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "data": {
            "ipAddress": "203.0.113.45",
            "abuseConfidenceScore": 100
        }
    }
    
    api = ThreatIntelAPI(api_key="fake_key_for_testing")
    
    # Act
    result = api.check_ip("203.0.113.45")
    
    # Assert
    assert result['ipAddress'] == "203.0.113.45"
    assert result['abuseConfidenceScore'] == 100
    mock_get.assert_called_once() # Proves our code actually tried to send the HTTP request