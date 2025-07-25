import re
import json


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
        Функция реализует поиск банковских операций у которых в описании
        есть заданная строка
    """

    search_split = search.split(" ")

    pattern = ""
    for i in range(len(search_split)):
        pattern += f"\w*\s*\w*\s*{search_split[i]}\.*\s*\w*"

    print(pattern)

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
