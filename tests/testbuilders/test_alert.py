import pytest
import urllib.parse
from cta.api.builders.alert import AlertAPIBuilder

def test_initialization_valid_output_type():
    builder = AlertAPIBuilder(outputType="json")
    assert builder.outputType == "json"

def test_initialization_invalid_output_type():
    with pytest.raises(ValueError, match="outputType must be either `xml` or `json`"):
        AlertAPIBuilder(outputType="html")


def test_build_route_status_api_url_valid():
    builder = AlertAPIBuilder(outputType="json")
    url = builder.buildRouteStatusAPIURL(
        type=["bus", "rail"],
        routeid=["22", "36"],
        stationid=["30120", "30121"]
    )
    # URL encode the expected parameters for comparison
    expected_type = urllib.parse.quote("bus,rail")
    expected_routeid = urllib.parse.quote("22,36")
    expected_stationid = urllib.parse.quote("30120,30121")
    
    # Assertions to check the correctness of the generated URL
    assert f"type={expected_type}" in url
    assert f"routeid={expected_routeid}" in url
    assert f"stationid={expected_stationid}" in url


def test_build_route_status_api_url_invalid_type():
    builder = AlertAPIBuilder(outputType="json")
    with pytest.raises(ValueError, match="`invalid` is not a valid input to parameter `type`"):
        builder.buildRouteStatusAPIURL(type=["bus", "invalid"])

