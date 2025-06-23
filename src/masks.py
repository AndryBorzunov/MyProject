def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера банковской карты"""
    if isinstance(card_number, int) == False:
        return "Неверный тип входных данных"

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
    account_number_str = str(account_number)

    mask_account_number = "**" + account_number_str[-4:]

    return mask_account_number
