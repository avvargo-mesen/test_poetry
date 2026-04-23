from typing import Any

import pytest

from src.decorators import log_decorator


# проверяет на ловлю ошибки
@log_decorator()
def example_function() -> None:
    raise ValueError


def test_log_decorator() -> None:
    with pytest.raises(ValueError):
        example_function()


# проверяет на верный вывод
@log_decorator()
def example_function_right() -> None:
    pass


def test_example_function_right(capsys: Any) -> None:
    example_function_right()
    captured = capsys.readouterr()
    assert captured.out == (
        "Function example_function_right started\n"
        "example_function_right ok\n"
        "Function example_function_right finished\n"
    )


# проверяет на верный вывод в файл
@log_decorator(filename="test_log")
def example_function_txt() -> None:
    pass


def test_log_decorator_txt() -> None:
    example_function_txt()
    with open("test_log", 'r') as file:
        content = file.read()
        assert "Function example_function_txt started" in content
        assert "example_function_txt ok" in content
        assert "Function example_function_txt finished" in content
