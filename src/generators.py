def filter_by_currency (transactions: list[dict], currency: str) -> Generator[dict]:
    '''Генератор возвращает транзакции, где валюта соответствует заданной.'''
    for d in transactions:
        if d["operationAmount"]["currency"]["name"] == currency:
            yield d

# yield list(filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions_list))

gen_currency = filter_by_currency([{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "RUB",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"},
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2019-08-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9823.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"}], "USD")

# first_item = next(gen_currency)
# print(first_item)
# second_item = next(gen_currency)
# print(second_item)


# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))

def transaction_descriptions(transactions: list[dict]) -> Generator[str]:
    '''Генератор возвращает описание каждой операции по очереди.'''
    for d in transactions:
        yield d["description"]

gen_descriptions = transaction_descriptions([{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "RUB",
                      "code": "RUB"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"},
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2019-08-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9823.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"}])

# first_item = next(gen_descriptions)
# print(first_item)
# second_item = next(gen_descriptions)
# print(second_item)
# third_item = next(gen_descriptions)
# print(third_item)

def card_number_generator(start: int, stop: int) -> Generator[str]:
    '''Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.'''
    card_number = ""
    card_number_new = ""
    for i in range(start, stop + 1):
        card_number = f"{i:016d}"
        card_number_1 = card_number[0:4]
        card_number_2 = card_number[4:8]
        card_number_3 = card_number[8:12]
        card_number_4 = card_number[12:16]
        card_number_new = f"{card_number_1} {card_number_2} {card_number_3} {card_number_4}"
        yield card_number_new

gen_card_number = card_number_generator(1, 5)

first_item = next(gen_card_number)
print(first_item)
second_item = next(gen_card_number)
print(second_item)
third_item = next(gen_card_number)
print(third_item)





