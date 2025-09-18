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