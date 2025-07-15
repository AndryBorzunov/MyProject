import json
import  os

from typing import Any, Dict, List


def load_Transactions(file_name: str) -> List[Dict[str, Any]]:
    """ Считывание транзакций, записанных в json формате из файла"""

    if not os.path.isfile(file_name):
        return []

    try:
        with open(file_name, encoding="utf-8") as file:
            transactions = json.load(file)
            if isinstance(transactions, list):
                return transactions
            else:
                return []
    except Exception as e:
        return []
