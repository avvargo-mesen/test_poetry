import os
from dotenv import load_dotenv
import requests


# Загрузка переменных из .env-файла
load_dotenv()


def convert_to_rubles(transaction: dict) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return float(amount)
    if currency == "USD" or currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        try:
            # Получение значения переменной API_KEY из .env-файла
            apilayer_token = os.getenv('API_KEY')
            # Создание заголовка с токеном доступа API
            headers = {
                'apikey': apilayer_token
            }
            # Отправка GET-запроса к API
            response = requests.get(url, headers=headers)
            # Обработка ответа
            data = response.json()
            # print(data)
            return float(data["result"])
        except requests.exceptions.ConnectionError:
            print("Connection Error. Please check your network connection.")
        except requests.exceptions.HTTPError:
            print("HTTP Error. Please check the URL.")
        except requests.exceptions.Timeout:
            print("Request timed out. Please check your internet connection.")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects. Please check the URL.")
        except requests.exceptions.RequestException:
            print("An error occurred. Please try again later.")

    return float(amount)


result = convert_to_rubles({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  })

print(result)