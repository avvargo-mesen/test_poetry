import json
from json import JSONDecodeError


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
