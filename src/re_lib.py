import re
from collections import Counter

def process_bank_search(data: list[dict], search: str) -> list[dict]:
    strings_new = []
    for dictionary in data:
        string_new = dictionary["description"]


        if search == "":
            return []
        else:
            transactions = re.findall(search, string_new, flags=re.IGNORECASE)
            if transactions == []:
                continue
            else:
                strings_new.append(dictionary)


    return strings_new


search = "Перевод с карты на карту"
data = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z',
            'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'},
           {'id': 3598919.0, 'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
            'currency_name': 'Peso',
            'currency_code': 'COP', 'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643',
            'description': 'Перевод с карты на карту'},
           {'id': 593027.0, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z',
            'amount': 30368.0, 'currency_name': 'Shilling', 'currency_code': 'TZS',
            'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710',
            'description': 'Перевод с карты на карту'}]

# result = process_bank_search(data, search)
# print(result)


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    dictionary_counted = Counter()

    for dictionary in data:
        category_new = dictionary["description"]

        if categories == []:
            return []
        else:
            for category in categories:
                if category in category_new:
                    dictionary_counted[category] += 1
                else:
                    continue

    return dictionary_counted

categories = ['Перевод с карты на карту', 'Перевод организации']


result1 = process_bank_operations(data, categories)
print(result1)










