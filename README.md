# Банковские операции - система обработки данных

Проект предоставляет инструменты для работы с банковскими операциями: маскирование номеров карт и счетов, фильтрация и сортировка транзакций.

## Структура проекта

```
project/
├── masks.py          # Функции маскирования номеров карт и счетов
├── widget.py         # Вспомогательные функции для работы с данными
├── processing.py     # Функции фильтрации и сортировки транзакций
└── README.md         # Документация проекта
```

## Установка и использование

### Требования
- Python 3.7+

### Установка
```bash
git clone <repository-url>
cd project
```

## Функции

### masks.py

#### `get_mask_card_number(card_number: str) -> str`
Маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

**Пример:**
```python
from masks import get_mask_card_number

card_number = "1234567812345678"
masked = get_mask_card_number(card_number)  # "1234 56** **** 5678"
```

#### `get_mask_account(account: str) -> str`
Маскирует номер счета, оставляя видимыми только последние 4 цифры.

**Пример:**
```python
from masks import get_mask_account

account = "12345678901234567890"
masked = get_mask_account(account)  # "**7890"
```

### widget.py

#### `mask_account_card(data: str) -> str`
Определяет тип данных (карта или счет) и применяет соответствующую маскировку.

**Примеры:**
```python
from widget import mask_account_card

# Для карты
masked_card = mask_account_card("Visa Platinum 1234567812345678")
# "Visa Platinum 1234 56** **** 5678"

# Для счета
masked_account = mask_account_card("Счет 12345678901234567890")
# "Счет **7890"
```

#### `get_date(date: str) -> str`
Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

**Пример:**
```python
from widget import get_date

formatted_date = get_date("2024-03-11T02:26:18.671407")
# "11.03.2024"
```

### processing.py

#### `filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]`
Фильтрует список транзакций по статусу.

**Пример:**
```python
from processing import filter_by_state

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2024-01-02'}
]

executed = filter_by_state(transactions)  # Только EXECUTED
canceled = filter_by_state(transactions, 'CANCELED')  # Только CANCELED
```

#### `sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]`
Сортирует транзакции по дате.

**Пример:**
```python
from processing import sort_by_date

sorted_desc = sort_by_date(transactions)  # По убыванию (новые сначала)
sorted_asc = sort_by_date(transactions, False)  # По возрастанию (старые сначала)
```

## Пример использования

```python
from masks import get_mask_card_number, get_mask_account
from widget import mask_account_card, get_date
from processing import filter_by_state, sort_by_date

# Маскирование данных
card_mask = get_mask_card_number("1234567812345678")
account_mask = get_mask_account("12345678901234567890")

# Обработка строки с данными
masked_data = mask_account_card("Visa Platinum 1234567812345678")

# Форматирование даты
formatted_date = get_date("2024-03-11T02:26:18.671407")

# Фильтрация и сортировка транзакций
transactions = [...]  # список словарей с транзакциями
executed_transactions = filter_by_state(transactions)
sorted_transactions = sort_by_date(executed_transactions)
```

## Обработка ошибок

Все функции включают проверки входных данных:
- Валидация длины номеров карт (16 цифр) и счетов (20 цифр)
- Проверка на наличие только цифр в номерах
- Обработка некорректных форматов дат

## Тестирование

Для тестирования функций можно использовать встроенные модули Python:

```python
import unittest
from masks import get_mask_card_number

class TestMasks(unittest.TestCase):
    def test_card_mask(self):
        self.assertEqual(get_mask_card_number("1234567812345678"), "1234 56** **** 5678")

if __name__ == '__main__':
    unittest.main()
```

## Лицензия

Проект распространяется под MIT License.