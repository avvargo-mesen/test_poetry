import pytest


@pytest.fixture
def my_list() -> list[dict]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def my_list_zero() -> list[dict]:
    return []


@pytest.fixture
def my_list_same_date() -> list[dict]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T08:21:33.419441'}
    ]


@pytest.fixture
def my_list_bad_date() -> list[dict]:
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': ' '},
        {},
]


@pytest.fixture
def list_by_currency() -> list[dict]:
    return [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"}, {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2019-08-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9823.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"}]


@pytest.fixture
def list_by_currency_empty() -> list[dict]:
    return []


@pytest.fixture
def transactions_for_search():
    return [
        {"description": "Перевод организации", "amount": 100},
        {"description": "Открытие вклада", "amount": 200},
        {"description": "Перевод с карты на карту", "amount": 300},
        {"description": "Оплата услуг", "amount": 400},
    ]

@pytest.fixture
def transactions_for_operations():
    return [
        {'description': 'Перевод организации'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Перевод с карты на карту'},
    ]

@pytest.fixture
def categories_for_operations():
    return ['Перевод с карты на карту', 'Перевод организации']

@pytest.fixture
def transactions_for_operations_not_my_category():
    return [
        {'description': 'Открытие'},
]