from unittest.mock import patch

from main import main


@patch('builtins.input')
def test_main(mock_input):
    """Проверка работы функции с файлом Json"""
    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "нет"]

    main()
