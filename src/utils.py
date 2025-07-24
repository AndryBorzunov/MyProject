import json
import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s : %(filename)s : %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions(file_name: str) -> List[Dict[str, Any]]:
    """Считывание транзакций, записанных в json формате из файла"""

    # if not os.path.isfile(file_name):
    #    return []

    try:
        with open(file_name, encoding="utf-8") as file:
            transactions = json.load(file)
            if isinstance(transactions, list):
                logger.info(f"Получено {len(transactions)} транзакций")
                return transactions
            else:
                logger.error("Некорректные данные")
                return []
    except Exception as e:
        logger.error(e)
        return []
