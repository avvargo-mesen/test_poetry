from typing import Any
from typing import Callable
from typing import Optional


def log_decorator(filename: Optional[str] = None) -> Callable:
    """Задает файл/консоль для логов"""
    def my_decorator(func: Callable) -> Callable:
        """Принимает декорируемую функцию"""
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Принимает аргументы декорируемой функции и возвращает результат"""
            start_message = f"Function {func.__name__} started"
            end_message = f"Function {func.__name__} finished"
            result = None
            try:
                result = func(*args, **kwargs)
                message = (f'{func.__name__} ok')
            except Exception as e:
                message = (f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
                raise e
            if filename is None:
                print(start_message)
                print(message)
                print(end_message)
            else:
                with open(filename, 'a') as file:
                    file.write(start_message + '\n')
                    file.write(message + '\n')
                    file.write(end_message + '\n')

            return result

        return wrapper

    return my_decorator
