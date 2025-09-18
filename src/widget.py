from masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета в строке."""
    if "счет" in data.lower():
        # Обработка счета
        parts = data.rsplit(" ", 1)
        if len(parts) != 2:
            return data  # Не удалось разделить, возвращаем как есть
        account_type, number = parts
        masked_number = get_mask_account(number)
        return f"{account_type} {masked_number}"
    else:
        # Обработка карты
        parts = data.rsplit(" ", 1)
        if len(parts) != 2:
            return data  # Не удалось разделить, возвращаем как есть
        card_type, number = parts
        masked_number = get_mask_card_number(number)
        return f"{card_type} {masked_number}"


def get_date(date: str) -> str:
    """принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
    и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    date_formatted = f"{day}.{month}.{year}"
    return date_formatted
