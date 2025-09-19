# Проект по обработке банковских данных

Проект предоставляет набор утилит для работы с банковскими данными: маскирование номеров карт и счетов, обработка транзакций и форматирование дат.

## Структура проекта

```
src/
├── masks.py          # Функции маскирования номеров карт и счетов
├── widget.py         # Утилиты для обработки строк с данными карт/счетов
└── processing.py     # Функции для фильтрации и сортировки транзакций
tests/
├── test_masks.py     # Тесты для модуля masks
├── test_widget.py    # Тесты для модуля widget
└── test_processing.py # Тесты для модуля processing
```

## Установка и запуск

1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Запустите тесты:
```bash
pytest -v
```

4. Запустите тесты с покрытием:
```bash
pytest --cov=src --cov-report=html
```

## Модуль `masks`

### Функции:

#### `get_mask_card_number(card_number: str) -> str`
Маскирует номер банковской карты по формату: `1234 56** **** 5678`

**Требования:**
- Номер должен содержать ровно 16 цифр
- Допускаются пробелы в номере (автоматически удаляются)
- Возвращает ValueError при невалидных данных

**Пример:**
```python
from src.masks import get_mask_card_number

masked = get_mask_card_number("1234567812345678")  # "1234 56** **** 5678"
```

#### `get_mask_account(account: str) -> str`
Маскирует номер банковского счета: показывает только последние 4 цифры

**Требования:**
- Номер должен содержать ровно 20 цифр
- Допускаются пробелы в номере
- Возвращает ValueError при невалидных данных

**Пример:**
```python
from src.masks import get_mask_account

masked = get_mask_account("12345678901234567890")  # "**7890"
```

## Модуль `widget`

### Функции:

#### `mask_account_card(data: str) -> str`
Автоматически определяет тип данных (карта или счет) и применяет соответствующую маску.

**Особенности:**
- Распознает слово "счет" в любом регистре
- Возвращает исходную строку при ошибках маскирования
- Поддерживает различные платежные системы

**Пример:**
```python
from src.widget import mask_account_card

masked_card = mask_account_card("Visa Platinum 1234567812345678")  # "Visa Platinum 1234 56** **** 5678"
masked_account = mask_account_card("Счет 12345678901234567890")    # "Счет **7890"
```

#### `get_date(date: str) -> str`
Преобразует дату из формата ISO в русский формат.

**Форматы:**
- Вход: `"2024-03-11T02:26:18.671407"`
- Выход: `"11.03.2024"`

**Пример:**
```python
from src.widget import get_date

formatted = get_date("2024-01-15T10:30:00.000")  # "15.01.2024"
```

## Модуль `processing`

### Функции:

#### `filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]`
Фильтрует список транзакций по статусу.

**Поддерживаемые статусы:**
- `"EXECUTED"` - выполненные
- `"PENDING"` - ожидающие
- `"CANCELED"` - отмененные

**Пример:**
```python
from src.processing import filter_by_state

transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2024-01-15T10:30:00.000"},
    {"id": 2, "state": "PENDING", "date": "2024-01-14T12:00:00.000"}
]

executed = filter_by_state(transactions, "EXECUTED")
```

#### `sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]`
Сортирует транзакции по дате.

**Параметры:**
- `reverse=True` - по убыванию (новые сначала)
- `reverse=False` - по возрастанию (старые сначала)

**Пример:**
```python
from src.processing import sort_by_date

sorted_transactions = sort_by_date(transactions)  # Новые транзакции first
```

## Тестирование

Проект включает comprehensive тестирование:

- ✅ Unit-тесты для всех функций
- ✅ Тестирование граничных случаев
- ✅ Тестирование ошибок и исключений
- ✅ Параметризованные тесты
- ✅ Покрытие кода >80%

**Запуск тестов:**
```bash
pytest tests/ -v
pytest --cov=src --cov-report=html
```

## Требования

- Python 3.7+
- pytest для тестирования
- pytest-cov для измерения покрытия

## Обработка ошибок

Все функции включают валидацию входных данных и выбрасывают соответствующие исключения:
- `ValueError` для невалидных номеров карт/счетов
- Возврат исходных данных при невозможности обработки
- Корректная обработка `None` и пустых значений