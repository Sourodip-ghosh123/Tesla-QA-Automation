import pytest
from utils.api_client import APIClient

def test_inventory_search():
    client = APIClient()
    params = {
        "model": "m3",
        "condition": "new",
        "arrangeby": "relevance",
        "market": "US"
    }
    response = client.get_inventory(params)
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) > 0

def test_invalid_inventory_search():
    client = APIClient()
    params = {
        "model": "invalid_model",
        "condition": "new",
        "market": "US"
    }
    response = client.get_inventory(params)
    assert response.status_code == 400
