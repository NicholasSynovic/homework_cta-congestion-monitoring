import pytest
from cta.api.builders.train import TrainAPIBuilder

@pytest.fixture
def train_api_builder():
    """Fixture to create an instance of TrainAPIBuilder."""
    return TrainAPIBuilder(key="test_key")

def test_buildArrivalsAPIURL_with_mapid(train_api_builder: TrainAPIBuilder):
    """Test buildArrivalsAPIURL with valid mapid."""
    url = train_api_builder.buildArrivalsAPIURL(mapid=12345)
    expected_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=test_key&outputType=json&mapid=12345"
    assert url == expected_url

def test_buildArrivalsAPIURL_with_stpid(train_api_builder: TrainAPIBuilder):
    url = train_api_builder.buildArrivalsAPIURL(stpid=67890)
    expected_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=test_key&outputType=json&stpid=67890"
    assert url == expected_url

def test_buildArrivalsAPIURL_with_mapid_and_stpid(train_api_builder: TrainAPIBuilder):
    url = train_api_builder.buildArrivalsAPIURL(mapid=12345, stpid=67890)
    expected_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=test_key&outputType=json&mapid=12345&stpid=67890"
    assert url == expected_url

def test_buildArrivalsAPIURL_with_max(train_api_builder: TrainAPIBuilder):
    url = train_api_builder.buildArrivalsAPIURL(mapid=12345, max=5)
    expected_url = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=test_key&outputType=json&mapid=12345&max=5"
    assert url == expected_url

def test_buildArrivalsAPIURL_with_invalid_params(train_api_builder: TrainAPIBuilder):
    with pytest.raises(ValueError, match="Either mapid or stpid must be set"):
        train_api_builder.buildArrivalsAPIURL()
