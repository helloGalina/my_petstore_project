import requests

BASE_URL = "https://petstore.swagger.io/v2"

class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params)

    def post(self, endpoint, json=None, data=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", json=json, data=data, headers=headers)

    def put(self, endpoint, json=None):
        return requests.put(f"{self.base_url}{endpoint}", json=json)

    def delete(self, endpoint, headers=None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)

