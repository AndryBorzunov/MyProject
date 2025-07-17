import json
from unittest.mock import patch

import pytest

from src.utils import load_transactions


@patch("builtins.open", create=True)
def test_load_transactions_empty(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = []
    assert load_transactions("test.txt") == []
    mock_open.assert_called_once_with("test.txt", encoding="utf-8")


@pytest.fixture
def data_input():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


@patch("builtins.open")
def test_load_transactions(mock_open, data_input):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps(data_input)
    assert load_transactions("test.txt") == data_input
    mock_open.assert_called_once_with("test.txt", encoding="utf-8")
