from typing import Any, Dict, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> iter:
    """
    Генератор транзакций, отфильтрованных по валюте операции
    """

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions) -> iter:
    """
    Принимает список транзакций и возвращает описание каждой транзакции
    по очереди
    """

    for transaction in transactions:
        if "description" not in transaction:
            raise ValueError("В словаре отсутствует ключ 'description'")

        yield transaction["description"]
