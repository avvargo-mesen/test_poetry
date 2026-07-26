# from src.masks import get_mask_account
# from src.masks import get_mask_card_number
from src.data_reader import read_csv_files
from src.data_reader import read_excel_files
from src.generators import filter_by_currency
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.re_lib import process_bank_search
from src.utils import read_json_file
from src.widget import get_date
from src.widget import mask_account_card

# if __name__ == '__main__':
#     # Проверка masks
#     get_mask_card_number(7000792289606361)
#     get_mask_account(7365410843013587430)
#
#     # Проверка utils
#     read_json_file("data/operations.json")


def main():
    """Объединяет функции + пользовательский интерфейс"""
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')
    guest_choice1 = input()
    while True:
        if guest_choice1 == '1':
            transactions = read_json_file("data/operations.json")
            print(transactions)
            break
        if guest_choice1 == '2':
            transactions = read_csv_files("data/transactions.csv")
            break
        if guest_choice1 == '3':
            transactions = read_excel_files("data/transactions_excel.xlsx")
            break
        else:
            print('Неверный выбор. Попробуйте снова.')
            guest_choice1 = input()

    print('Введите статус,по которому необходимо выполнить фильтрацию. Доступные статусы: EXECUTED, CANCELED, PENDING')

    while True:
        guest_choice2 = input()
        guest_choice2_upp = guest_choice2.upper()
        if guest_choice2_upp == 'EXECUTED':
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break
        if guest_choice2_upp == 'CANCELED':
            print('Операции отфильтрованы по статусу "CANCELED"')
            break
        if guest_choice2_upp == 'PENDING':
            print('Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f'Статус операции {guest_choice2_upp} недоступен. Введите досупный статус')

    transactions = filter_by_state(transactions, guest_choice2_upp)

    print(transactions)

    print('Отсортировать операции по дате? Да/Нет')

    while True:
        guest_choice3 = input()
        guest_choice3_upp = guest_choice3.upper()
        if guest_choice3_upp == "ДА":
            print('Отсортировать по возрастанию или по убыванию?')

            while True:
                guest_choice4 = input()
                guest_choice4_upp = guest_choice4.upper()
                if guest_choice4_upp == "ПО ВОЗРАСТАНИЮ":
                    transactions = sort_by_date(transactions)
                    break
                elif guest_choice4_upp == "ПО УБЫВАНИЮ":
                    transactions = sort_by_date(transactions, True)
                    break
                else:
                    print(f'Выбор {guest_choice4_upp} недоступен. Введите "ПО ВОЗРАСТАНИЮ" или "ПО УБЫВАНИЮ')

            break

        elif guest_choice3_upp == "НЕТ":
            break
        else:
            print(f'Выбор {guest_choice3_upp} недоступен. Введите "ДА" или "НЕТ')

    print(transactions)

    print('Выводить только рублевые транзакции? Да/Нет')

    while True:
        guest_choice5 = input()
        guest_choice5_upp = guest_choice5.upper()
        if guest_choice5_upp == "ДА":
            transactions = list(filter_by_currency(transactions, "RUB"))
            break
        elif guest_choice5_upp == "НЕТ":
            break
        else:
            print(f'Выбор {guest_choice5_upp} недоступен. Введите "ДА" или "НЕТ')
            print(transactions)

    print(transactions)

    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')

    while True:
        guest_choice6 = input()
        guest_choice6_upp = guest_choice6.upper()
        if guest_choice6_upp == "ДА":
            print("Введите нужное слово")
            print(f"Количество транзакций до поиска: {len(transactions)}")
            guest_choice7 = input()
            guest_choice7_upp = guest_choice7.upper()
            transactions = process_bank_search(transactions, guest_choice7_upp)
            break
        elif guest_choice6_upp == "НЕТ":
            break
        else:
            print(f'Выбор {guest_choice6_upp} недоступен. Введите "ДА" или "НЕТ')

    if transactions == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(transactions)}')

    for transaction in transactions:
        date_new = transaction["date"]
        guest_date = get_date(date_new)
        guest_description = transaction["description"]
        if "operationAmount" in transaction:
            guest_amount = transaction["operationAmount"]["amount"]
            guest_currency = transaction["operationAmount"]["currency"]["code"]
        else:
            guest_amount = transaction["amount"]
            guest_currency = transaction["currency_code"]
        to_mask = transaction["to"]
        guest_card_to = mask_account_card(to_mask)
        if "from" in transaction:
            from_mask = transaction.get("from")
            if from_mask and isinstance(from_mask, str):
                guest_card_from = mask_account_card(from_mask)
            else:
                guest_card_from = "Нет данных"
            print(f"{guest_date} {guest_description}\n"
                  f"{guest_card_from} -> {guest_card_to}\n"
                  f"Сумма: {guest_amount} {guest_currency}")
        else:
            print(f"{guest_date} {guest_description}\n{guest_card_to}\nСумма: {guest_amount} {guest_currency}")


if __name__ == "__main__":
    main()
