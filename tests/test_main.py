from unittest.mock import patch

from main import main


@patch('builtins.input')
def test_main1(mock_input):
    """Проверка работы функции с файлом Json"""
    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "нет"]

    main()


@patch('builtins.input')
def test_main1_1(mock_input):
    """Проверка работы функции с файлом Json"""
    mock_input.side_effect = ["1", "EXECUTED", "да", "по возрастанию", "да", "нет"]

    main()


@patch('builtins.input')
def test_main2(mock_input):
    """Проверка работы функции с файлом Json"""
    mock_input.side_effect = ["1", "CANCELED", "нет", "нет", "нет"]

    main()


@patch('builtins.input')
def test_main2_1(mock_input):
    """Проверка работы функции с файлом Json"""
    mock_input.side_effect = ["1", "CANCELED", "да", "по возрастанию", "да", "нет"]

    main()


@patch('builtins.input')
def test_main3(mock_input):
    """Проверка работы функции с файлом Json"""
    mock_input.side_effect = ["1", "PENDING", "нет", "нет", "нет"]

    main()


@patch('builtins.input')
def test_main3_1(mock_input):
    """Проверка работы функции с файлом Json"""
    mock_input.side_effect = ["1", "PENDING", "да", "по возрастанию", "да", "нет"]

    main()
