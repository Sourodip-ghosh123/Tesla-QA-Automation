import requests
from .config import API_BASE_URL

class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL

    def get_inventory(self, params):
        url = f"{self.base_url}/inventory-results"
        return requests.get(url, params=params)
