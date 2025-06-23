import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_of_dicts():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dicts_invalid():
    return [
        {"id": 41428829, "status": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "stats": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "stat": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "status": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "stat, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(list_of_dicts, stat, expected):
    assert filter_by_state(list_of_dicts, stat) == expected


def test_filter_by_state_invalid(list_of_dicts_invalid):
    with pytest.raises(ValueError):
        filter_by_state(list_of_dicts_invalid)


def test_filter_by_state_empty():
    with pytest.raises(ValueError):
        filter_by_state([])
