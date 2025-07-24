from unittest.mock import patch

import pytest

from src.external_api import get_amount_rub


@pytest.mark.parametrize(
    "data_input, result",
    [
        (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
            75957.58,
        ),
    ],
)
@patch("requests.get")
def test_get_amount_rub(mock_get, data_input, result):
    mock_get.return_value.json.return_value = {"result": result}
    assert get_amount_rub(data_input) == result
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        {"to": "RUB", "from": "USD", "amount": "8221.37"},
        headers={"apikey": "q6VoZdwfem7JJpcI6f0L9X9bDd36FWAh"},
    )


@pytest.mark.parametrize(
    "data_input, result",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            31957.58,
        ),
        (
            {
                "id": 587085106,
                "state": "EXECUTED",
                "date": "2018-03-23T10:45:06.972075",
                "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            },
            48223.05,
        ),
    ],
)
def test_get_amount_rub_rub(data_input, result):
    assert get_amount_rub(data_input) == result


def test_get_amount_rub_empty():
    with pytest.raises(ValueError):
        get_amount_rub({})


@pytest.fixture
def incorrect_data():
    return {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amounts": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
    }


def test_get_amount_rub_error(incorrect_data):
    with pytest.raises(ValueError):
        get_amount_rub(incorrect_data)
