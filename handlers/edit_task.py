from typing import TYPE_CHECKING
from utils import input_with_validation, validate_date_format, validate_priority

if TYPE_CHECKING:
    from models import TaskManager  # Импортируем только для проверки типов


def edit_task(manager: "TaskManager") -> None:
    """
    Функция для редактирования задачи в менеджере задач.

    :param manager: Экземпляр класса TaskManager, который управляет списком задач.
    """
    # Получение ID задачи для редактирования
    try:
        task_id: int = int(input("\nВведите ID задачи для редактирования: "))
    except ValueError:
        print("\nОшибка: ID задачи должен быть числом.")
        return

    # Поиск задачи с указанным ID
    task = next((task for task in manager.tasks if task.id == task_id), None)
    if not task:
        print(f"\nЗадача с ID {task_id} не найдена.")
        return

    print("\nПримечание: Если поле не нужно менять, оставьте строку пустой.")

    # Редактирование названия
    title: str = input_with_validation(
        prompt=f"Название ({task.title}): ",
        error_message="",
        validation_func=lambda x: True  # Пустой ввод допустим
    ).strip()
    if title:
        task.title = title

    # Редактирование описания
    description: str = input_with_validation(
        prompt=f"Описание ({task.description}): ",
        error_message="",
        validation_func=lambda x: True
    ).strip()
    if description:
        task.description = description

    # Редактирование категории
    category: str = input_with_validation(
        prompt=f"Категория ({task.category}): ",
        error_message="",
        validation_func=lambda x: True
    ).strip()
    if category:
        task.category = category

    # Редактирование срока выполнения
    due_date: str = input_with_validation(
        prompt=f"Срок ({task.due_date}): ",
        error_message="Ошибка: Некорректный формат даты. Введите дату в формате гггг-мм-дд.",
        validation_func=lambda x: validate_date_format(x, "%Y-%m-%d") if x else True
    ).strip()
    if due_date:
        task.due_date = due_date

    # Редактирование приоритета
    priority: str = input_with_validation(
        prompt=f"Приоритет ({task.priority}): ",
        error_message="Ошибка: Введите 1, 2, 3 или оставьте пустым.",
        validation_func=lambda x: validate_priority(x) if x else True
    ).strip()
    if priority:
        priority_map = {"1": "Низкий", "2": "Средний", "3": "Высокий"}
        task.priority = priority_map.get(priority, task.priority)

    # Сохранение изменений
    manager.save_tasks()
    print("\nЗадача обновлена.")
