import pytest
from utils.api_client import APIClient

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def order_id(client):
    order_data = {
        "petId": 0,
        "quantity": 1,
        "shipDate": "2024-12-15T11:41:54.117Z",
        "status": "placed",
        "complete": True
    }
    response = client.post("/store/order", json=order_data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    return response.json()["id"]

def test_post_order(order_id): # Проверка успешного создания заказа
    assert order_id is not None, "Order ID was not created"

def test_get_order_by_id(client, order_id): # Проверка получения заказа по ID
    response = client.get(f"/store/order/{order_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["id"] == order_id
