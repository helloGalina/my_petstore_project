import pytest
from utils.api_client import APIClient

client = APIClient()

@pytest.fixture
def new_pet(): # Создает тестового питомца и возвращает его ID
    pet_data = {
        "id": 12345,
        "name": "TestPet",
        "status": "available"
    }
    response = client.post("/pet", json=pet_data)
    assert response.status_code == 200, f"Failed to create pet: {response.text}"
    yield pet_data["id"]
    # Удаляем питомца после завершения теста
    client.delete(f"/pet/{pet_data['id']}")

def test_get_pet_by_id(new_pet): # Тест получения питомца по ID (GET /pet/{petId})
    response = client.get(f"/pet/{new_pet}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["id"] == new_pet

def test_create_pet(): # Тест создания нового питомца (POST /pet)
    pet_data = {
        "id": 54321,
        "name": "NewTestPet",
        "status": "available"
    }
    response = client.post("/pet", json=pet_data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["id"] == pet_data["id"]
    assert response.json()["name"] == pet_data["name"]
    # Удаляем созданного питомца
    client.delete(f"/pet/{pet_data['id']}")

def test_update_pet(new_pet): # Тест обновления питомца (PUT /pet)
    updated_data = {
        "id": new_pet,
        "name": "UpdatedTestPet",
        "status": "sold"
    }
    response = client.put("/pet", json=updated_data)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["name"] == "UpdatedTestPet"
    assert response.json()["status"] == "sold"

def test_delete_pet(new_pet): # Тест удаления питомца (DELETE /pet/{petId})
    response = client.delete(f"/pet/{new_pet}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.json()["message"] == str(new_pet)
    # Проверяем, что питомец удален
    response = client.get(f"/pet/{new_pet}")
    assert response.status_code == 404, "Pet was not deleted"