import pytest
from src.masks import get_mask_card_number, get_mask_account


# Тесты для get_mask_card_number
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_with_spaces():
    assert get_mask_card_number("1234 5678 1234 5678") == "1234 56** **** 5678"


@pytest.mark.parametrize(
    "card_number",
    [
        "1234",  # Слишком короткий номер
        "12345678123456789",  # Слишком длинный номер
        "12345678abcd5678",  # Не только цифры
        "",  # Пустая строка
    ],
)
def test_get_mask_card_number_invalid(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


# Тесты для get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("00001111222233334444", "**4444"),
    ],
)
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_with_spaces():
    assert get_mask_account("1234 5678 9012 3456 7890") == "**7890"


@pytest.mark.parametrize(
    "account_number",
    [
        "1234",  # Слишком короткий номер
        "123456789012345678901",  # Слишком длинный номер
        "12345678abcd56789012",  # Не только цифры
        "",  # Пустая строка
    ],
)
def test_get_mask_account_invalid(account_number):
    with pytest.raises(ValueError):
        get_mask_account(account_number)


# Тесты для проверки сообщений об ошибках
def test_get_mask_card_number_error_messages():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1234")
    assert "16 цифр" in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("1234abcd5678efgh")
    assert "только из цифр" in str(exc_info.value)


def test_get_mask_account_error_messages():
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("1234")
    assert "20 цифр" in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        get_mask_account("1234abcd5678efgh9012")
    assert "только из цифр" in str(exc_info.value)
