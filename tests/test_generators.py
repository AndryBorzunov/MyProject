import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize("currency, filter_transactions_index", [("USD", [0, 1, 3]), ("RUB", [2, 4])])
def test_filter_by_currency(transactions, currency, filter_transactions_index):
    generator = filter_by_currency(transactions, currency)
    assert next(generator) == transactions[filter_transactions_index[0]]
    assert next(generator) == transactions[filter_transactions_index[1]]


def test_filter_by_currency_currency_off(transactions):
    generator = filter_by_currency(transactions, "BYN")
    with pytest.raises(StopIteration):
        next(generator)


@pytest.fixture
def bad_data():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07"},
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


def test_filter_by_currency_nodata(bad_data):
    generator = filter_by_currency(bad_data, "BYN")
    with pytest.raises(ValueError):
        next(generator)


def test_filter_by_currency_empty():
    generator = filter_by_currency([], "BYN")
    with pytest.raises(ValueError):
        next(generator)


@pytest.fixture
def descriptions():
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_transaction_description(transactions, descriptions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == descriptions[0]
    assert next(generator) == descriptions[1]
    assert next(generator) == descriptions[2]
    assert next(generator) == descriptions[3]
    assert next(generator) == descriptions[4]
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_description_nodata(bad_data):
    generator = transaction_descriptions(bad_data)
    with pytest.raises(ValueError):
        next(generator)


def test_transaction_description_empty():
    generator = transaction_descriptions([])
    with pytest.raises(ValueError):
        next(generator)


@pytest.mark.parametrize(
    "start, stop, card_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, card_numbers):
    generator = card_number_generator(start, stop)
    assert next(generator) == card_numbers[0]
    assert next(generator) == card_numbers[1]
    assert next(generator) == card_numbers[2]
    assert next(generator) == card_numbers[3]
    assert next(generator) == card_numbers[4]
    with pytest.raises(StopIteration):
        next(generator)
