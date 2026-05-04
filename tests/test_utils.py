import pytest
from src.utils import read_json_file


def test_read_json_empty_file():
    """тест на пустой файл"""
    assert read_json_file("tests/test_empty.json") == []


def test_read_json_file_dict():
    """тест не содержит список"""
    assert read_json_file("tests/test_not_list.json") == []


def test_read_json_no_file():
    """тест нет переданного в аргументы файла"""
    assert read_json_file("non_existent_file.json") == []


def test_read_json_good_file():
    """тест есть переданный в аргументы файла"""
    assert read_json_file("tests/test_operations.json") == [
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
