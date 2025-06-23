from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Обрабатывает информацию о карте или счету и выводит маскировку"""

    account_card_list = account_card.split()
    if len(account_card_list) < 2:
        raise ValueError("Некорректный ввод")

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
    if len(date_time) < 10:
        raise ValueError("Некорректный ввод")

    date_time_list = date_time.split("T")
    date_list = date_time_list[0].split("-")

    if len(date_list[0]) != 4 or not date_list[0].isdigit() or not date_list[1].isdigit():
        raise ValueError("Некорректный ввод")

    date_list.reverse()

    return ".".join(date_list)
