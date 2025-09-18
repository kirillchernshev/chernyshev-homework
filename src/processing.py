def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    """
    if not transactions:
        return []

    filtered_transactions = []
    for transaction in transactions:
        if isinstance(transaction, dict) and transaction.get("state") == state:
            filtered_transactions.append(transaction)

    return filtered_transactions


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по дате с обработкой ошибок.
    """
    if not transactions:
        return []

    # Фильтруем словари, у которых есть ключ 'date'
    valid_transactions = [t for t in transactions if "date" in t]

    return sorted(valid_transactions, key=lambda x: x["date"], reverse=reverse)
