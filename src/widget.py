def mask_account_card(type_card_account_numbers: str) -> str:
    '''Функция возвращает строку с замаскированным номером'''
    list_type = []
    str_type = ""
    list_number = []
    str_number =""
    splited_string = type_card_account_numbers.split(" ")

    #print(splited_string)

    for item in splited_string: # смотрим на каждый символ в строке
        if item.isalpha():
            list_type.append(item) # если это буква, добавляем в лист с названием типа(карта или счет)
            str_type = " ".join(list_type)
            #print(list_type)
            #print(str_type)
        if item.isdigit():      # если это число, добавляем в лист с номером
            list_number.append(item)
            str_number = ''.join(list_number)
            #print(str_number)
            if len(str_number) == 16: # включаем маскировку для карты
                #print(str_number)
                from masks import get_mask_card_number
                #print(get_mask_card_number(int(str_number)))
                #print(str_type + " " + get_mask_card_number(int(str_number)))
                return str_type + " " + get_mask_card_number(int(str_number))
            elif len(str_number) == 20: # включаем маскировку для счета
                #print(str_number)
                from masks import get_mask_account
                #print(get_mask_account(int(str_number)))
                return str_type + " " + get_mask_account(int(str_number))
            else:
                return "Введите номер заново"

result = mask_account_card("Счет 73654108430135874455")
print(result)


#def get_date(current_date: str) -> str:
#'''Функиця возвращает дату в нужном формате'''
#
#
