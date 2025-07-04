import pytest

from src.widget import get_date, mask_account_card


@pytest.fixture
def input_data():
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


@pytest.mark.parametrize(
    "index, expected",
    [
        (0, "Maestro 1596 83** **** 5199"),
        (1, "Счет **9589"),
        (2, "MasterCard 7158 30** **** 6758"),
        (3, "Счет **5560"),
        (4, "Visa Classic 6831 98** **** 7658"),
        (5, "Visa Platinum 8990 92** **** 5229"),
        (6, "Visa Gold 5999 41** **** 6353"),
        (7, "Счет **4305"),
    ],
)
def test_mask_account_card(input_data, index, expected):
    assert mask_account_card(input_data[index]) == expected


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("Cчет 64686473678894779589")


def test_mask_account_card_empty():
    with pytest.raises(ValueError):
        mask_account_card("Счет ")


def test_mask_account_card_empty2():
    with pytest.raises(ValueError):
        mask_account_card("64686473678894779589")


@pytest.mark.parametrize(
    "input_dt, output_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-01-19T15:06:11.564321", "19.01.2025"),
    ],
)
def test_get_date(input_dt, output_date):
    assert get_date(input_dt) == output_date


def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("2547_05-15T11:54:12.976554")
