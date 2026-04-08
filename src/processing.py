from src.widget import get_date


def filter_by_state(dict_list: list, state: str = 'EXECUTED') -> list:
    """Функция возвращает список словарей, у которых ключ state соответствует указанному значению"""
    new_list = []
    for d in dict_list:
        if d.get("state") == state:
            new_list.append(d)

    return new_list


# result = filter_by_state ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], state='EXECUTED')
# print(result)


def sort_by_date(dict_list: list, descending: bool = False) -> list:
    """Функция возвращает список словарей, отсортированных по дате"""
    filtered = []
    for item in dict_list:
        date_value = item.get('date')
        if date_value and get_date(date_value) != "Введите корректную дату":
            filtered.append(item)
    return sorted(filtered, key=lambda x: x['date'], reverse=descending)

# result = sort_by_date([{'id': 41428829, 'state': 'EXECUTED'}, {},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.2416893'}])
# print(result)

# result = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
# print(result)
