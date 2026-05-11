from typing import Any
from unittest.mock import patch

import requests

from src.external_api import convert_to_rubles


# Верные данные
@patch('requests.get')
def test_convert_to_rubles(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {"result": 16442.784}
    assert convert_to_rubles({
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }) == 16442.784
    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert args[0] == 'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37'


# Ошибка соединения
def test_convert_to_rubles_connection_error() -> None:
    with patch('requests.get') as mock_response:
        mock_response.side_effect = requests.exceptions.ConnectionError()

        result = convert_to_rubles({
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        })
        assert result == 8221.37


# Нет ответа от сервера долгое время
def test_convert_to_rubles_timeout() -> None:
    with patch('requests.get') as mock_response:
        mock_response.side_effect = requests.exceptions.Timeout()

        result = convert_to_rubles({
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        })
        assert result == 8221.37


# Слишком много обращений
def test_convert_to_rubles_many_redirects() -> None:
    with patch('requests.get') as mock_response:
        mock_response.side_effect = requests.exceptions.TooManyRedirects()

        result = convert_to_rubles({
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        })
        assert result == 8221.37


# Остальные ошибки
def test_convert_to_rubles_request_exception() -> None:
    with patch('requests.get') as mock_response:
        mock_response.side_effect = requests.exceptions.RequestException()

        result = convert_to_rubles({
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        })
        assert result == 8221.37
