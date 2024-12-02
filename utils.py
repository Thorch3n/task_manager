from datetime import datetime


def input_with_validation(prompt, error_message, validation_func):
    """
    Функция ввода с проверкой.
    :param prompt: Сообщение для ввода.
    :param error_message: Сообщение об ошибке.
    :param validation_func: Функция для проверки ввода.
    :return: Валидированный ввод.
    """
    while True:
        value = input(prompt).strip()
        if validation_func(value):
            return value
        print(error_message)


def validate_non_empty(value):
    """Проверяет, что значение не пустое."""
    return bool(value)


def validate_date_format(value, date_format="%d-%m-%Y"):
    """Проверяет, что дата соответствует формату."""
    try:
        datetime.strptime(value, date_format)
        return True
    except ValueError:
        return False


def validate_priority(value):
    """Проверяет, что приоритет введен корректно (1, 2 или 3)."""
    return value in {'1', '2', '3'}
