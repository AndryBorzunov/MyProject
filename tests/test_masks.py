import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_numbers():
    return [
        1596837868705199,
        7158300734726758,
        6831982476737658,
        8990922113665229,
        5999414228426353,
        "5444333389008765",
    ]


@pytest.mark.parametrize(
    "index,expected",
    [
        (0, "1596 83** **** 5199"),
        (1, "7158 30** **** 6758"),
        (2, "6831 98** **** 7658"),
        (3, "8990 92** **** 5229"),
        (4, "5999 41** **** 6353"),
        (5, "Неверный тип входных данных"),
    ],
)
def test_get_mask_card_number(card_numbers, index, expected):
    assert get_mask_card_number(card_numbers[index]) == expected


def test_get_mask_card_number_invalid():
    with pytest.raises(ValueError):
        get_mask_card_number(12)


def test_get_mask_card_number_invalid2():
    with pytest.raises(ValueError):
        get_mask_card_number(12855657755757474747474747)


def test_get_mask_card_number_negative():
    with pytest.raises(ValueError):
        get_mask_card_number(-5444333389008765)


@pytest.mark.parametrize(
    "index, expected",
    [(0, "**5199"), (1, "**6758"), (2, "**7658"), (3, "**5229"), (4, "**6353"), (5, "Неверный тип входных данных")],
)
def test_get_mask_account(card_numbers, index, expected):
    assert get_mask_account(card_numbers[index]) == expected


def test_get_mask_account_invalid():
    with pytest.raises(ValueError):
        get_mask_account(12)


def test_get_mask_account_invalid2():
    with pytest.raises(ValueError):
        get_mask_account(12855657755757474747474747)


def test_get_mask_account_negative():
    with pytest.raises(ValueError):
        get_mask_account(-5444333389008765)
