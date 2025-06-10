from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card

if __name__ == "__main__":

    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(7365410840135874305))

    # Домашнее задание 9.2
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Platinum 8990922113665229"))