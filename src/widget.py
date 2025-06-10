from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Обрабатывает информацию о карте или счету и выводит маскировку"""

    account_card_list = account_card.split()
    account_type_list = []

    is_card = True
    for word in account_card_list:
        if word.isdigit():
            if is_card:
                account_type_list.append(get_mask_card_number(int(word)))
            else:
                account_type_list.append(get_mask_account(int(word)))
        else:
            account_type_list.append(word)
            if word == "Счет":
                is_card = False

    return " ".join(account_type_list)


def get_date(date_time: str) -> str:
    """Изменение формата даты"""
    date_time_list = date_time.split("T")
    date_list = date_time_list[0].split("-")

    date_list.reverse()

    return ".".join(date_list)
