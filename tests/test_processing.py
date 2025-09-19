import pytest
from src.processing import filter_by_state, sort_by_date


# Фикстуры для тестовых данных
@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000"},
        {"id": 2, "state": "PENDING", "date": "2024-01-14T12:00:00.000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-13T15:45:00.000"},
        {"id": 4, "state": "CANCELED", "date": "2024-01-12T09:15:00.000"},
        {"id": 5, "state": "EXECUTED", "date": "2024-01-11T08:00:00.000"},
    ]


@pytest.fixture
def transactions_with_missing_keys():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000"},
        {"id": 2},  # Нет state и date
        {"state": "PENDING"},  # Нет date
        {"date": "2024-01-12T09:15:00.000"},  # Нет state
    ]


@pytest.fixture
def transactions_with_same_dates():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000"},
        {"id": 2, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000"},
        {"id": 3, "state": "PENDING", "date": "2024-01-14T12:00:00.000"},
    ]


@pytest.fixture
def empty_transactions():
    return []


# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3, 5]),
    ("PENDING", [2]),
    ("CANCELED", [4]),
    ("NON_EXISTENT", []),  # Несуществующий статус
])
def test_filter_by_state(sample_transactions, state, expected_ids):
    result = filter_by_state(sample_transactions, state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_empty_list(empty_transactions):
    result = filter_by_state(empty_transactions, "EXECUTED")
    assert result == []


def test_filter_by_state_none_input():
    result = filter_by_state(None, "EXECUTED")
    assert result == []


def test_filter_by_state_missing_state_key(transactions_with_missing_keys):
    result = filter_by_state(transactions_with_missing_keys, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 1


# Тесты для sort_by_date
def test_sort_by_date_descending(sample_transactions):
    result = sort_by_date(sample_transactions)
    expected_order = [1, 2, 3, 4, 5]  # От новых к старым
    assert [item["id"] for item in result] == expected_order


def test_sort_by_date_ascending(sample_transactions):
    result = sort_by_date(sample_transactions, reverse=False)
    expected_order = [5, 4, 3, 2, 1]  # От старых к новым
    assert [item["id"] for item in result] == expected_order


def test_sort_by_date_same_dates(transactions_with_same_dates):
    result = sort_by_date(transactions_with_same_dates)
    assert [item["id"] for item in result] == [1, 2, 3]


def test_sort_by_date_empty_list(empty_transactions):
    result = sort_by_date(empty_transactions)
    assert result == []


def test_sort_by_date_none_input():
    result = sort_by_date(None)
    assert result == []


def test_sort_by_date_missing_date_key(transactions_with_missing_keys):
    result = sort_by_date(transactions_with_missing_keys)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert "date" in result[1]