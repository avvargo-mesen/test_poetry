from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(type_card_account_numbers: str) -> str:
    '''Функция возвращает строку с замаскированным номером'''
    list_type = []
    str_type = ""
    list_number = []
    str_number = ""
    splited_string = type_card_account_numbers.split(" ")

    for item in splited_string:
        if item.isalpha():
            list_type.append(item)
            str_type = " ".join(list_type)
        if item.isdigit():
            list_number.append(item)
            str_number = ''.join(list_number)
            if len(str_number) == 16:

                return str_type + " " + get_mask_card_number(int(str_number))
            elif len(str_number) == 20:

                return str_type + " " + get_mask_account(int(str_number))
            else:

                return "Введите номер заново"

    return "Введите номер заново"  # добавила, т.к. ругался mypy


# result = mask_account_card("Счет 73654108430135874305")
# print(result)


def get_date(current_date: str) -> str:
    '''Функиця возвращает дату в нужном формате'''
    if current_date == " " or len(current_date) != 26:
        return "Введите корректную дату"
    else:
        slice_date = current_date[:10]
        new_date_format = f"{slice_date[-2:]}.{slice_date[5:7]}.{slice_date[:4]}"

    return new_date_format


# result = get_date("1999-10-11T02:26:18.671407")
# print(result)
