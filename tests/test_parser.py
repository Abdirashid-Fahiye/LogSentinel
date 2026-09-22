import pytest
from pathlib import Path
from src.logsentinel.parser import LogParser

def test_parse_file_extracts_valid_lines():
    # Arrange: Get cross-platform path to the mock log
    mock_log_path = Path(__file__).parent / "mock_access.log"
    parser = LogParser(str(mock_log_path))
    
    # Act
    results = parser.parse_file()
    
    # Assert
    assert len(results) == 3, "Parser should extract 3 valid lines and skip the 1 corrupted line"
    
    # Check the first normal request
    assert results[0]['ip'] == "192.168.1.50"
    assert results[0]['method'] == "GET"
    assert results[0]['url'] == "/index.html"
    
    # Check the SQLi request
    assert results[1]['ip'] == "203.0.113.45"
    assert results[1]['url'] == "/login?user=' OR 1=1--"