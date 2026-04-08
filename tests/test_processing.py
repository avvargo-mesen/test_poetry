# тесты для filter_by_state и sort_by_date

# Задание 1

# Тестирование фильтрации списка словарей по заданному статусу state.
# Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
# Параметризация тестов для различных возможных значений статуса state.

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize("state, expected", [
    ('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    ('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]),
    ('CONFIRMED', []),
    ('REJECTED', []),
    ('EXPIRED', [])
])
def test_filter_by_state(my_list: list, state: str, expected: list) -> None:
    """Список по заданному статусу + различные возможные значения state"""
    assert filter_by_state(my_list, state) == expected


@pytest.mark.parametrize("state, expected", [
    ('EXECUTED', []),
    ('CANCELED', [])
])
def test_filter_by_state_zero(my_list_zero: list, state: str, expected: list) -> None:
    """проверка при отсуствии словарей с нужным статусом"""
    assert filter_by_state(my_list_zero, state) == expected

# Задание 2

# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
# Проверка корректности сортировки при одинаковых датах.
# Тесты на работу функции с некорректными или нестандартными форматами дат.


@pytest.mark.parametrize("descending, expected", [
    (True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ])
])
def test_sort_by_date(my_list: list, descending: bool, expected: list) -> None:
    """проверка сортировки по убыванию и возрастанию"""
    assert sort_by_date(my_list, descending) == expected


@pytest.mark.parametrize("descending, expected", [
    (True, [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    (False, [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
])
def test_sort_by_date_same_date(my_list_same_date: list, descending: bool, expected: list) -> None:
    """Проверка сортировки при одинаковых датах"""
    assert sort_by_date(my_list_same_date, descending) == expected


# Некорректные/нестандартные даты
def test_sort_by_date_bad_date(my_list_bad_date: list) -> None:
    """Проверка неверных дат"""
    assert sort_by_date(my_list_bad_date, descending=False) == []
