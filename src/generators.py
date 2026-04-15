def filter_by_currency (transactions: list[dict], currency: str) -> Generator:
    '''Функция возвращает транзакции, где валюта соответствует заданной'''
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
