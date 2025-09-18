def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает маску номера"""
    cleaned_number = card_number.replace(" ", "")
    if not cleaned_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр!")

    if len(cleaned_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр!")

    first_part = cleaned_number[:6]  # Первые 6 цифр
    last_part = cleaned_number[-4:]  # Последние 4 цифры

    masked_number = f"{first_part[:4]} {first_part[4:6]}** **** {last_part}"

    return masked_number


def get_mask_account(account: str) -> str:
    """Функция принимает номер счета и возвращает маску номера"""
    cleaned_account = account.replace(" ", "")
    if not cleaned_account.isdigit():
        raise ValueError("Номер аккаунта должен состоять только из цифр!")

    if len(cleaned_account) != 20:
        raise ValueError("Номер аккаунта должен содержать 20 цифр!")

    masked_account = f"**{cleaned_account[-4:]}"
    return masked_account
