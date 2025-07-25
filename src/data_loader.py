from typing import Any, Dict, Hashable, List

import pandas as pd


def load_data_csv(path_csv: str, is_head: bool=True) -> List[Dict[Hashable, Any]]:
    """Функция загружает таблицу данных из файла .csv"""

    try:
        transactions_csv = pd.read_csv(path_csv + "/" + "transactions.csv", sep=";")
        print(transactions_csv.shape)

        if is_head:
            head_csv = transactions_csv.head()
            transactions_json = head_csv.to_dict(orient="records")
        else:
            transactions_json = transactions_csv.to_dict(orient="records")
        return transactions_json

    except FileNotFoundError as file:
        print(f"Файл {file} не найден")
        return []


def load_data_excel(path_excel: str) -> List[Dict[Hashable, Any]]:
    """Функция загружает таблицу из файла excel (.xlsx)"""

    try:
        transactions_xls = pd.read_excel(path_excel + "/" + "transactions_excel.xlsx")
        print(transactions_xls.shape)
        head_xls = transactions_xls.head()
        transactions_json = head_xls.to_dict(orient="records")
        return transactions_json

    except FileNotFoundError as file:
        print(f"Файл {file} не найден")
        return []
