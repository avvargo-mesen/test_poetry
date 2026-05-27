import pandas as pd

from unittest.mock import Mock
from unittest.mock import patch
from src.data_reader import read_csv_files
from src.data_reader import read_excel_files

@patch('pandas.read_csv')
def test_read_csv_files(mock_read_csv):
    mock_df = pd.DataFrame([{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                     'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
                                     'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                     'description': 'Перевод организации'}, {'id': 3598919.0, 'state': 'EXECUTED',
                                    'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso',
                                    'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                    'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                    {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
                                     'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS',
                                     'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710',
                                     'description': 'Перевод с карты на карту'}])
    mock_read_csv.return_value=mock_df
    assert read_csv_files('any.csv') == [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                     'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
                                     'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                     'description': 'Перевод организации'}, {'id': 3598919.0, 'state': 'EXECUTED',
                                    'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso',
                                    'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                    'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                    {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
                                     'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS',
                                     'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710',
                                     'description': 'Перевод с карты на карту'}]


@patch('pandas.read_csv')
def test_read_csv_files_empty(mock_read_csv):
    mock_df = pd.DataFrame([])
    mock_read_csv.return_value=mock_df
    assert read_csv_files('any.csv') == []







@patch('pandas.read_excel')
def test_read_excel_files(mock_read_excel):
    mock_df = pd.DataFrame([{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                     'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
                                     'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                     'description': 'Перевод организации'}, {'id': 3598919.0, 'state': 'EXECUTED',
                                    'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso',
                                    'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                    'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                    {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
                                     'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS',
                                     'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710',
                                     'description': 'Перевод с карты на карту'}])
    mock_read_excel.return_value=mock_df
    assert read_excel_files('any.excel') == [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
                                     'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
                                     'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
                                     'description': 'Перевод организации'}, {'id': 3598919.0, 'state': 'EXECUTED',
                                    'date': '2020-12-06T23:00:58Z', 'amount': 29740.0, 'currency_name': 'Peso',
                                    'currency_code': 'COP', 'from': 'Discover 3172601889670065',
                                    'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
                                    {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
                                     'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS',
                                     'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710',
                                     'description': 'Перевод с карты на карту'}]


@patch('pandas.read_excel')
def test_read_excel_files_empty(mock_read_excel):
    mock_df = pd.DataFrame([])
    mock_read_excel.return_value=mock_df
    assert read_excel_files('any.csv') == []