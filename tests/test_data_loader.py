from unittest.mock import patch

import pytest

from src.data_loader import load_data_csv, load_data_excel


@patch("pandas.read_csv")
def test_load_data_csv_empty(mock_csv_reader):
    mock_file = mock_csv_reader.return_value.head.return_value
    mock_file.to_dict.return_value = []
    assert load_data_csv("path_test") == []
    mock_csv_reader.assert_called_once_with("path_test/transactions.csv", sep=";")


@pytest.fixture
def data_output():
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


@patch("pandas.read_csv")
def test_load_data_csv(mock_csv_reader, data_output):
    mock_file = mock_csv_reader.return_value.head.return_value
    mock_file.to_dict.return_value = data_output
    assert load_data_csv("path_test") == data_output
    mock_csv_reader.assert_called_once_with("path_test/transactions.csv", sep=";")


def test_load_data_csv_error():
    assert load_data_csv("path_test") == []


@patch("pandas.read_excel")
def test_load_data_excel(mock_excel_reader, data_output):
    mock_file = mock_excel_reader.return_value.head.return_value
    mock_file.to_dict.return_value = data_output
    assert load_data_excel("path_test") == data_output
    mock_excel_reader.assert_called_once_with("path_test/transactions_excel.xlsx")


@patch("pandas.read_excel")
def test_load_data_excel_empty(mock_excel_reader):
    mock_file = mock_excel_reader.return_value.head.return_value
    mock_file.to_dict.return_value = []
    assert load_data_excel("path_test") == []
    mock_excel_reader.assert_called_once_with("path_test/transactions_excel.xlsx")


def test_load_data_excel_error():
    assert load_data_excel("path_test") == []
