# Petstore API Tests

## Описание
Проект включает функциональные тесты для API Petstore. 

## Запуск тестов
1. Установите зависимости:
pip install -r requirements.txt


## Запустите тесты
pytest -sv tests

## Тестируемые методы
- `POST /pet` — Создание питомца
- `GET /pet/{petId}` — Получение питомца по ID
- `PUT /pet` — Обновление данных питомца
- `DELETE /pet/{petId}` — Удаление питомца