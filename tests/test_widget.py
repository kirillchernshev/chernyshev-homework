import pytest
from src.widget import mask_account_card, get_date
from src.masks import get_mask_account, get_mask_card_number


# Фикстура для тестовых данных
@pytest.fixture
def sample_card_data():
    return "Visa Platinum 1234567812345678"


@pytest.fixture
def sample_account_data():
    return "Счет 12345678901234567890"


# Тесты для mask_account_card
@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "Счет 12345678901234567890",
            f"Счет {get_mask_account('12345678901234567890')}",
        ),
        (
            "Visa Platinum 1234567812345678",
            f"Visa Platinum {get_mask_card_number('1234567812345678')}",
        ),
        (
            "MasterCard 1111222233334444",
            f"MasterCard {get_mask_card_number('1111222233334444')}",
        ),
        (
            "Maestro 1234567812345678",
            f"Maestro {get_mask_card_number('1234567812345678')}",
        ),
        (
            "счет 12345678901234567890",
            f"счет {get_mask_account('12345678901234567890')}",
        ),
    ],
)
def test_mask_account_card_valid(input_data, expected):
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_data",
    [
        "Счет 1234",  # Невалидный номер счета
        "Visa 1234",  # Невалидный номер карты
        "Просто текст",  # Нет номера
        "",  # Пустая строка
    ],
)
def test_mask_account_card_invalid_numbers(input_data):
    assert mask_account_card(input_data) == input_data


def test_mask_account_card_no_space():
    assert mask_account_card("Счет1234567890") == "Счет1234567890"


# Тесты для get_date
@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-01-15T10:30:00.000", "15.01.2024"),
        ("2023-12-31T23:59:59.999", "31.12.2023"),
        ("2020-02-29T00:00:00.000", "29.02.2020"),  # Високосный год
        ("1999-01-01T00:00:00.000", "01.01.1999"),
    ],
)
def test_get_date_valid(input_date, expected):
    assert get_date(input_date) == expected


@pytest.mark.parametrize(
    "input_date",
    [
        "",  # Пустая строка
        "2024-01-15",  # Неполный формат
        "invalid-date",  # Невалидная дата
    ],
)
def test_get_date_edge_cases(input_date):
    result = get_date(input_date)
    assert isinstance(result, str)
    if input_date == "":
        assert result == ".."
