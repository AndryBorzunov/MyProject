from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Выборка словарей из списка словарей с заданным статусом"""
    if len(list_of_dicts) == 0:
        raise ValueError("Нет данных")

    filter_list = []
    for dict_item in list_of_dicts:
        if not "state" in dict_item:
            raise ValueError("В словаре отсутствует ключ 'state'")

        if dict_item["state"] == state:
            filter_list.append(dict_item)

    return filter_list


def sort_by_date(list_of_dicts: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортировка полученного списка по дате
    по умолчанию - сортировка по убыванию
    """

    return sorted(list_of_dicts, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
