def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера банковской карты"""
    if not isinstance(card_number, int):
        return "Неверный тип входных данных"

    if card_number < 0:
        raise ValueError("Некорректный ввод")

    card_number_str = str(abs(card_number))
    if len(card_number_str) != 16:
        raise ValueError("Некорректный ввод")

    mask_card_number = ""
    index = 0
    for item in card_number_str:
        if index % 4 == 0 and index > 0:
            mask_card_number += " "
        if 5 < index < 12:
            mask_card_number += "*"
        else:
            mask_card_number += item
        index += 1

    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Маскировка номера банковского счета"""
    if not isinstance(account_number, int):
        return "Неверный тип входных данных"

    if account_number < 0:
        raise ValueError("Некорректный ввод")

    account_number_str = str(account_number)
    if len(account_number_str) > 20 or len(account_number_str) < 8:
        raise ValueError("Некорректный ввод")

    mask_account_number = "**" + account_number_str[-4:]

    return mask_account_number
