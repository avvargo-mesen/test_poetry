# Задание 1


def get_mask_card_number(card_number: int) -> str:
    """Функция преобразует номер карты в замаскированный номер"""
    new_list = []
    str_card_number = str(card_number)
    mask_card_number_total = ""

    if len(str_card_number) != 16:
        return "Введите номер карты заново"
    else:
        for i, num in enumerate(str_card_number):
            current_index = i
            if 0 <= current_index <= 5:
                new_list.append(num)
            elif 5 < current_index < 12:
                new_list.append("*")
            else:
                new_list.append(num)
        slice_result1 = new_list[0:4]
        slice_result2 = new_list[4:8]
        slice_result3 = new_list[8:12]
        slice_result4 = new_list[12:]
        mask_result1 = "".join(slice_result1)
        mask_result2 = "".join(slice_result2)
        mask_result3 = "".join(slice_result3)
        mask_result4 = "".join(slice_result4)
        mask_card_number_total = mask_result1 + " " + mask_result2 + " " + mask_result3 + " " + mask_result4

    return mask_card_number_total


result = get_mask_card_number(7000792289606361)
print(result)


# Задание 2


def get_mask_account(account_number: int) -> str:
    """Функция преобразует номер счета и возвращает его в формате **XXXX"""
    temp_list = []
    new_list = ["*", "*"]
    result_list = []
    result_str = ""
    str_account_number = str(account_number)

    if len(str_account_number) != 20:
        return "Введите номер счета заново"
    else:
        for i, num in enumerate(str_account_number):
            temp_list.append(num)
            slice_result = temp_list[-4:]
            result_list = new_list + slice_result
            result_str = "".join(result_list)

    return result_str


result = get_mask_account(73654108430135874305)
print(result)
