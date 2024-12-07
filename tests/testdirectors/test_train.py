import pytest
from unittest.mock import MagicMock, patch
from requests import Response
from cta.api.builders.train import TrainAPIBuilder
from cta.api.directors.train import TrainAPIDirector
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath("cta/api/directors/train.py")))


@pytest.fixture
def api_key():
    return "test_api_key"


@pytest.fixture
def train_api_director(api_key):
    return TrainAPIDirector(key=api_key)


def test_initialization(api_key):
    director = TrainAPIDirector(key=api_key)
    assert isinstance(director.builder, TrainAPIBuilder)
    assert director.builder.key == api_key


@patch("cta.api.directors.train.get")  # Adjust the patch path to match your codebase
def test_get_arrivals(mock_get, train_api_director):
    # Mock the builder method to return a valid mock URL
    train_api_director.builder.buildRouteStatusAPIURL = MagicMock(return_value="http://mock_url")
    
    # Mock the GET request response
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success"}
    mock_get.return_value = mock_response

    # Call the method
    response = train_api_director.getArrivals()

    # Assert that the mock GET was called with the correct parameters
    mock_get.assert_called_once_with(url="http://mock_url", timeout=60)

    # Additional assertions
    assert response.status_code == 200
    assert response.json() == {"status": "success"}



@patch("cta.api.directors.train.get")
def test_get_follow_this_train(mock_get, train_api_director):
    # Mock the builder method
    train_api_director.builder.buildFollowThisTrainAPIURL = MagicMock(return_value="http://mock_url")  # Add scheme

    # Mock the GET request
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"train": "details"}
    mock_get.return_value = mock_response

    # Call the method
    response = train_api_director.getFollowThisTrain()

    # Assert mock was called
    mock_get.assert_called_once_with(url="http://mock_url", timeout=60)
    assert response.status_code == 200
    assert response.json() == {"train": "details"}

@patch("cta.api.directors.train.get")
def test_get_locations(mock_get, train_api_director):
    # Mock the builder method
    train_api_director.builder.buildLocationsAPIURL = MagicMock(return_value="mock_url")

    # Mock the GET request
    mock_response = MagicMock(spec=Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"locations": ["location1", "location2"]}
    mock_get.return_value = mock_response

    # Call the method
    response = train_api_director.getLocations()

    # Assertions
    train_api_director.builder.buildLocationsAPIURL.assert_called_once()
    mock_get.assert_called_once_with(url="mock_url", timeout=60)
    assert response.status_code == 200
    assert response.json() == {"locations": ["location1", "location2"]}
