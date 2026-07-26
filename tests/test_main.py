import pytest
import pandas as pd
from main import main

from unittest.mock import patch, Mock

@patch('builtins.input')
def test_main(mock_input):
    mock_input.side_effect = ["1", "EXECUTED", "нет", "нет", "нет"]

    main()
