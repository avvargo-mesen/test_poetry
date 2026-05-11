import json
import logging

from json import JSONDecodeError

logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler('utils.log')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.DEBUG)

logger_utils.debug('Debug message')
logger_utils.info('Info message')
logger_utils.warning('Warning message')
logger_utils.error('Error message')
logger_utils.critical('Critical message')


def read_json_file(filename: str) -> list[dict]:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)

        if type(data) is list:
            return data

        else:
            return []

    except FileNotFoundError:
        # Файл не найден
        return []

    except JSONDecodeError:
        # Файл пустой
        return []

    # except Exception:
    #     # Общий блок для всех остальных исключений
    #     return []

# result = read_json_file("../data/operations.json")
# print(result)
