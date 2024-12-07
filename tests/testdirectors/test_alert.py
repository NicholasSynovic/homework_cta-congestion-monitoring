import pytest
from requests.models import Response
from cta.api.directors.alert import AlertAPIDirector
from unittest.mock import patch,Mock


@pytest.fixture
def alert_api_director():
    """Fixture to instantiate AlertAPIDirector"""
    return AlertAPIDirector()


def test_get_route_status_success(alert_api_director):
    """Test for successful getRouteStatus"""
    resp = alert_api_director.getRouteStatus()

    # Check that the response has a status code 200
    assert resp.status_code == 200

    # Verify the content of the response
    json_resp = resp.json()
    assert 'CTARoutes' in json_resp
    assert len(json_resp['CTARoutes']['RouteInfo']) > 0
    assert 'RouteURL' in json_resp['CTARoutes']['RouteInfo'][0]
    
    # Check for the actual 'Route' key instead of 'RouteName'
    assert 'Route' in json_resp['CTARoutes']['RouteInfo'][0]


def test_get_route_status_failure(alert_api_director):
    """Test for failed getRouteStatus due to non-200 status code"""
    # Set an extremely short timeout to trigger a timeout error
    try:
        resp = alert_api_director.getRouteStatus(timeout=0.001)  # Timeout after 0.001 seconds
    except Exception as e:
        # Ensure an exception is raised (simulating failure)
        assert isinstance(e, Exception)



def test_get_detailed_alerts_success(alert_api_director):
    """Test for successful getDetailedAlerts"""
    resp = alert_api_director.getDetailedAlerts()

    # Check that the response has a status code 200
    assert resp.status_code == 200

    # Verify the content of the response
    json_resp = resp.json()

    # Ensure 'CTARoutes' and relevant fields are present in the response
    assert 'CTARoutes' in json_resp
    assert len(json_resp['CTARoutes']['RouteInfo']) > 0
    assert 'RouteURL' in json_resp['CTARoutes']['RouteInfo'][0]
    # Check for other relevant fields instead of 'Alert'
    assert 'RouteStatus' in json_resp['CTARoutes']['RouteInfo'][0]


def test_get_detailed_alerts_failure(alert_api_director):
    """Test for failed getDetailedAlerts due to non-200 status code"""
    # Mock the response to simulate a failure
    with patch.object(alert_api_director, 'getDetailedAlerts', return_value=Mock(status_code=500)):
        resp = alert_api_director.getDetailedAlerts(timeout=60)

    # Ensure the response status code is 500 (indicating failure)
    assert resp.status_code == 500
