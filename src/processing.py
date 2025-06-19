from datetime import datetime
from typing import List


def filter_by_state(list_of_dicts: List, state: str = "EXECUTED") -> List:
    """Выборка словарей из списка словарей с заданным статусом"""
    filter_list = []
    for dict_item in list_of_dicts:
        if dict_item["state"] == state:
            filter_list.append(dict_item)

    return filter_list


def sort_by_date(list_of_dicts: List, reverse: bool = True) -> List:
    """Сортировка полученного списка по дате
    по умолчанию - сортировка по убыванию
    """

    return sorted(list_of_dicts, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
