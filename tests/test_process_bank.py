import pytest

from src.process_bank import process_bank_operations, process_bank_search


@pytest.fixture
def list_of_dicts():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29Z", "description": "Перевод организации"},
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58Z",
            "description": "Перевод с карты на карту",
        },
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25Z", "description": "Открытие вклада"},
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33Z",
            "description": "Перевод со счета на счет",
        },
        {
            "id": 45847598,
            "state": "CANCELED",
            "date": "2019-07-03T08:21:33Z",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.mark.parametrize(
    "search, description",
    [
        (
            "вклад",
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25Z",
                    "description": "Открытие вклада",
                },
            ],
        ),
        (
            "перевод",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29Z",
                    "description": "Перевод организации",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58Z",
                    "description": "Перевод с карты на карту",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33Z",
                    "description": "Перевод со счета на счет",
                },
                {
                    "id": 45847598,
                    "state": "CANCELED",
                    "date": "2019-07-03T08:21:33Z",
                    "description": "Перевод с карты на карту",
                },
            ],
        ),
        (
            "на карту",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58Z",
                    "description": "Перевод с карты на карту",
                },
                {
                    "id": 45847598,
                    "state": "CANCELED",
                    "date": "2019-07-03T08:21:33Z",
                    "description": "Перевод с карты на карту",
                },
            ],
        ),
        (
            "возврат",
            [],
        ),
    ],
)
def test_process_bank_search(list_of_dicts, search, description):
    assert process_bank_search(list_of_dicts, search) == description


@pytest.fixture
def result():
    return {
        "Перевод организации": 1,
        "Перевод с карты на карту": 2,
        "Открытие вклада": 1,
        "Перевод со счета на счет": 1,
    }


def test_process_bank_operations(list_of_dicts, result):
    assert process_bank_operations(list_of_dicts) == result
