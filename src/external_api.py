import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_amount_rub(transaction: Dict[str, Any]) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если сумма транзакции в другой валюте, обращается к интернет-сервису для конвертации
    """
    if len(transaction) == 0:
        raise ValueError("Нет данных")

    if "operationAmount" not in transaction:
        raise ValueError("В словаре отсутствует ключ 'operationAmount'")

    if "currency" not in transaction["operationAmount"]:
        raise ValueError("В словаре отсутствует ключ 'currency'")

    if "code" not in transaction["operationAmount"]["currency"]:
        raise ValueError("В словаре отсутствует ключ 'code'")

    if "amount" not in transaction["operationAmount"]:
        raise ValueError("В словаре отсутствует ключ 'amount'")

    amount = transaction["operationAmount"]["amount"]
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return float(amount)

    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {"to": "RUB", "from": currency_code, "amount": amount}
        headers = {"apikey": API_KEY}
        response = requests.get(url, params, headers=headers)
        # if (response.status_code == 200):
        data = response.json()
        return float(data["result"])
        # else:
        # raise response.raise_for_status()
