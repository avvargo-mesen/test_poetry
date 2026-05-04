import pytest
import requests
from src.external_api import convert_to_rubles
from unittest.mock import Mock, patch

from unittest.mock import patch
import requests


# def get_github_user_info(username):
#     response = requests.get(f'https://api.github.com/users/{username}')
#     return response.json()

@patch('requests.get')
def test_convert_to_rubles(mock_get):
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


def test_convert_to_rubles_connection_error():
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

def test_convert_to_rubles_timeout():
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

def test_convert_to_rubles_many_redirects():
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

def test_convert_to_rubles_connection_error():
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

def test_convert_to_rubles_request_exception():
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

