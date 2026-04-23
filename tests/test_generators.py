import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions

# функция корректно фильтрует транзакции по заданной валюте
def test_filter_by_currency(list_by_currency: list) -> None:
    generator = filter_by_currency(list_by_currency, "USD")
    assert next(generator) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                               'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                               'to': 'Счет 11776614605963066702'}
    assert next(generator) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-08-30T02:08:58.425572',
                               'operationAmount': {'amount': '9823.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                               'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                               'to': 'Счет 11776614605963066702'}


# функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют
def test_filter_by_currency_empty(list_by_currency: list) -> None:
    generator = filter_by_currency(list_by_currency, "FRK")
    assert list(generator) == []


# пустой список
def test_filter_by_currency_no_list(list_by_currency_empty: list) -> None:
    generator = filter_by_currency(list_by_currency_empty, "USD")
    assert list(generator) == []


# функция возвращает корректные описания для каждой транзакции + пустой список
@pytest.mark.parametrize("transactions, expected", [([{
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
              "to": "Счет 75651667383060284188"},
    {
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
        "to": "Счет 11776614605963066702"}], ["Перевод организации", "Перевод со счета на счет",
                                              "Перевод организации"]), ([], [])])
def test_transaction_descriptions(transactions: list[dict], expected: list[str]) -> None:
    assert list(transaction_descriptions(transactions)) == expected


# генератор выдает правильные номера карт в заданном диапазоне
def test_card_number_generator() -> None:
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


# корректность форматирования номеров карт
def test_card_number_generator_firmat() -> None:
    generator = card_number_generator(1, 3)
    for card in generator:
        assert len(card) == 19
        assert card[4] == ' ' and card[9] == ' ' and card[14] == ' '


# крайние значения диапазона и завершние генерации
def test_card_number_generator_stop() -> None:
    generator = card_number_generator(100, 100)
    assert next(generator) == "0000 0000 0000 0100"

    with pytest.raises(StopIteration):
        next(generator)
