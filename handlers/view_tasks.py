from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import TaskManager


def view_tasks(manager: "TaskManager") -> None:
    """
    Отображает список всех задач.

    :param manager: Экземпляр класса TaskManager, содержащий список задач.
    """
    tasks = manager.tasks

    if not tasks:
        print("\nСписок задач пуст.")
    else:
        print("\nСписок всех задач:")
        for task in tasks:
            # Преобразование задачи в словарь и вывод
            print(f"- {task.to_dict()}")


def view_tasks_by_category(manager: "TaskManager") -> None:
    """
    Отображает список задач, принадлежащих указанной категории.

    :param manager: Экземпляр класса TaskManager, содержащий список задач.
    """
    # Получение категории от пользователя
    category: str = input("\nВведите категорию: ").strip()

    # Фильтрация задач по категории
    tasks = [task for task in manager.tasks if task.category.lower() == category.lower()]

    if not tasks:
        print(f"\nНет задач в категории '{category}'.")
    else:
        print(f"\nСписок задач в категории '{category}':")
        for task in tasks:
            # Преобразование задачи в словарь и вывод
            print(f"- {task.to_dict()}")
