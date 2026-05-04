from json import JSONDecodeError
from typing import Any
from unittest.mock import patch

from src.utils import read_json_file

# def test_read_json_empty_file():
#     """тест на пустой файл"""
#     assert read_json_file("tests/test_empty.json") == []
#
#
# def test_read_json_no_file():
#     """тест нет переданного в аргументы файла"""
#     assert read_json_file("non_existent_file.json") == []
#
# def test_read_json_file_dict():
#     """тест не содержит список"""
#     assert read_json_file("tests/test_not_list.json") == []
#
#
# def test_read_json_good_file():
#     """тест есть переданный в аргументы файла"""
#     assert read_json_file("tests/test_operations.json") == [
#         {
#             "id": 441945886,
#             "state": "EXECUTED",
#             "date": "2019-08-26T10:50:58.294041",
#             "operationAmount": {
#                 "amount": "31957.58",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Maestro 1596837868705199",
#             "to": "Счет 64686473678894779589"
#         }]


# Пустой файл
@patch('json.load')
def test_read_json_empty_file(mock_empty: Any) -> None:
    mock_empty.return_value = []
    assert read_json_file("any_path") == []


# Файл не найден
@patch('builtins.open')
def test_read_json_no_file(mock_no_file: Any) -> None:
    mock_no_file.side_effect = FileNotFoundError
    assert read_json_file("any_path") == []


# Невозможно декодировать файл
@patch('builtins.open')
@patch('json.load')
def test_read_json_decode(mock_decode: Any, mock_open: Any) -> None:
    mock_decode.side_effect = JSONDecodeError("Expecting value", "", 0)
    assert read_json_file("any_path") == []


# В файле не список (другой тип данных)
@patch('json.load')
def test_read_json_file_dict(mock_dict: Any) -> None:
    mock_dict.return_value = {}
    assert read_json_file("any_path") == []


# В файле верные данные
@patch('builtins.open')
@patch('json.load')
def test_read_json_good_file(mock_empty: Any, mock_open: Any) -> None:
    mock_empty.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]
    assert read_json_file("any_path") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]
