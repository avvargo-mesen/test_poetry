import pytest

from src.decorators import log_decorator

@log_decorator()
def example_function():
    raise ValueError

def test_log_decorator():
    with pytest.raises(ValueError):
        example_function()

@log_decorator()
def example_function_right():
    pass

def test_example_function_right(capsys):
    example_function_right()
    captured = capsys.readouterr()
    assert captured.out == ("Function example_function_right started\nexample_function_right ok\nFunction example_function_right finished\n")

@log_decorator(filename="test_log")
def example_function_txt():
    pass

def test_log_decorator_txt():
    example_function_txt()
    with open("test_log", 'r') as file:
        content = file.read()
        assert "Function example_function_txt started" in content
        assert "example_function_txt ok" in content
        assert "Function example_function_txt finished" in content