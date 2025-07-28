import json
import re
from collections import Counter
from typing import Any, Dict


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция реализует поиск банковских операций у которых в описании
    есть заданная строка
    """

    search_split = search.split(" ")

    pattern = ""
    for i in range(len(search_split)):
        pattern += f"\\w*\\s*\\w*\\s*{search_split[i]}\\.*\\s*\\w*"

    # print(pattern)

    search_datas = []
    for item in data:

        if "description" not in item:
            item_str = json.dumps(item, ensure_ascii=False)
        else:
            item_str = str(item["description"])

        result = re.search(pattern, item_str, re.IGNORECASE)

        if result is None:
            continue
        else:
            search_datas.append(item)

    return search_datas


def process_bank_operations(data: list[dict], categories: list) -> Dict[Any, int]:
    """
    Функция для выборки данных о количестве операций в каждой категории
    """

    result = dict()

    description_list = [item["description"] for item in data]

    counted = Counter(description_list)

    for key, value in counted.items():
        result[key] = value

    return result
