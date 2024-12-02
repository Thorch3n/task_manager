from typing import TYPE_CHECKING
from utils import input_with_validation, validate_non_empty, validate_date_format, validate_priority

if TYPE_CHECKING:
    from models import TaskManager  # Импортируем только для проверки типов


def add_task(manager: "TaskManager") -> None:
    """
    Функция для добавления новой задачи в менеджер задач.

    :param manager: Экземпляр класса TaskManager, который управляет списком задач.
    """
    # Запрашиваем название задачи с обязательной проверкой на непустой ввод
    title: str = input_with_validation(
        prompt="\nНазвание: ",
        error_message="Ошибка: Название не может быть пустым.",
        validation_func=validate_non_empty
    )

    # Запрашиваем описание задачи с обязательной проверкой на непустой ввод
    description: str = input_with_validation(
        prompt="Описание: ",
        error_message="Ошибка: Описание не может быть пустым.",
        validation_func=validate_non_empty
    )

    # Запрашиваем категорию задачи с обязательной проверкой на непустой ввод
    category: str = input_with_validation(
        prompt="Категория: ",
        error_message="Ошибка: Категория не может быть пустой.",
        validation_func=validate_non_empty
    )

    # Запрашиваем срок выполнения задачи с проверкой на корректный формат даты
    due_date: str = input_with_validation(
        prompt="Срок (дд-мм-гггг): ",
        error_message="Ошибка: Некорректный формат даты. Введите дату в формате дд-мм-гггг.",
        validation_func=lambda x: validate_date_format(x, "%d-%m-%Y")
    )

    # Запрашиваем приоритет задачи с проверкой на допустимые значения (1, 2, 3)
    priority: str = input_with_validation(
        prompt="Приоритет (1 - Низкий, 2 - Средний, 3 - Высокий): ",
        error_message="Ошибка: Введите 1, 2 или 3.",
        validation_func=validate_priority
    )

    # Сопоставляем числовое значение приоритета с текстовым описанием
    priority_map = {"1": "Низкий", "2": "Средний", "3": "Высокий"}
    priority_text: str = priority_map[priority]

    # Добавляем задачу через метод менеджера задач
    manager.add_task(title, description, category, due_date, priority_text)

    print("\nЗадача добавлена!")
