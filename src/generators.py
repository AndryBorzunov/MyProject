from typing import Any, Dict, List, Generator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Any | None, Any, None]:
    """Генератор транзакций, отфильтрованных по валюте операции"""

    if len(transactions) == 0:
        raise ValueError("Нет данных")

    for transaction in transactions:
        if "operationAmount" not in transaction:
            raise ValueError("В словаре отсутствует ключ 'operationAmount'")

        if "currency" not in transaction["operationAmount"]:
            raise ValueError("В словаре отсутствует ключ 'currency")

        if "code" not in transaction["operationAmount"]["currency"]:
            raise ValueError("В словаре отсутствует ключ 'code")

        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[Any | None, Any, None]:
    """Принимает список транзакций и возвращает описание каждой транзакции по очереди"""

    if len(transactions) == 0:
        raise ValueError("Нет данных")

    for transaction in transactions:
        if "description" not in transaction:
            raise ValueError("В словаре отсутствует ключ 'description'")

        yield transaction["description"]


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Generator[Any | None, Any, None]:
    """
    Генератор может сгенерировать номера карт в заданном диапазоне номеров
    """

    for gen_num in range(start, stop + 1):
        len_num = len(str(gen_num))
        if len_num <= 16:
            len_zero = 16 - len_num
            card_number = "0" * len_zero + str(gen_num)
            card_number = card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[-4:]
            yield card_number
