from typing import Any, Dict, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> iter:
    """
    Генератор транзакций, отфильтрованных по валюте операции
    """

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
