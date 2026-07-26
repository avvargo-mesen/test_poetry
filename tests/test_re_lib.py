import pytest
from src.re_lib import process_bank_search, process_bank_operations

# def test_something():
#     assert функция_которую_тестируем(аргументы) == ожидаемый_результат
#
# @pytest.mark.parametrize("входные_данные, ожидаемый_результат", [
#     (данные_1, результат_1),
#     (данные_2, результат_2),
# ])
# def test_функция(входные_данные, ожидаемый_результат):
#     assert функция(входные_данные) == ожидаемый_результат


# Верное слово в поиске
def test_process_bank_search_exact(transactions_for_search):
    result = process_bank_search(transactions_for_search, "Перевод")
    assert len(result) == 2

# Слово в поиске др. регистра
def test_process_bank_search_dif_letters(transactions_for_search):
    result = process_bank_search(transactions_for_search, "открытие")
    assert len(result) == 1

# Тест: слово не найдено
def test_process_bank_search_not_found(transactions_for_search):
    result = process_bank_search(transactions_for_search, "Покупка")
    assert result == []

# Тест: пустая строка поиска
def test_process_bank_search_empty(transactions_for_search):
    result = process_bank_search(transactions_for_search, "")
    assert result == []

def test_process_bank_operations(transactions_for_operations, categories_for_operations):
    result = process_bank_operations(transactions_for_operations, categories_for_operations)
    assert result == {"Перевод с карты на карту": 2, "Перевод организации": 1}

def test_process_bank_operations_not_my_category(transactions_for_operations_not_my_category, categories_for_operations):
    result = process_bank_operations(transactions_for_operations_not_my_category, categories_for_operations)
    assert result == {}

def test_process_bank_operations_empty_category(transactions_for_operations_not_my_category):
    result = process_bank_operations(transactions_for_operations_not_my_category, [])
    assert result == []