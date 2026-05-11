import json
import logging
from json import JSONDecodeError

logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.DEBUG)

# logger_utils.debug('Debug message')
# logger_utils.info('Info message')
# logger_utils.warning('Warning message')
# logger_utils.error('Error message')
# logger_utils.critical('Critical message')


def read_json_file(filename: str) -> list[dict]:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger_utils.info('Файл для записи открыт')
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)

        if type(data) is list:
            logger_utils.info('Список словарей успешно создан')
            return data

        else:
            logger_utils.error('Тип данных не список')
            return []

    except FileNotFoundError:
        # Файл не найден
        logger_utils.error('Файл с данными не найден')
        return []

    except JSONDecodeError:
        # Файл пустой
        logger_utils.error('Файл с данными пуст')
        return []

    # except Exception:
    #     # Общий блок для всех остальных исключений
    #     return []

# result = read_json_file("../data/operations.json")
# print(result)

# result = read_json_file("data/operations.json")
# print(result)
