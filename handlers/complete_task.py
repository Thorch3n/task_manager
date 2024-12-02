from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import TaskManager  # Импортируем только для проверки типов


def complete_task(manager: "TaskManager") -> None:
    """
    Функция для отметки задачи как выполненной.

    :param manager: Экземпляр класса TaskManager, который управляет списком задач.
    """
    # Запрос ID задачи для отметки как выполненной
    try:
        task_id: int = int(input("\nВведите ID выполненной задачи: "))
    except ValueError:
        print("\nОшибка: ID задачи должен быть числом.")
        return

    # Поиск задачи с заданным ID в списке задач
    task = next((task for task in manager.tasks if task.id == task_id), None)
    if not task:
        print(f"\nЗадача с ID {task_id} не найдена.")
        return

    # Отмечаем задачу как выполненную
    task.status = "Выполнена"
    manager.save_tasks()
    print("\nЗадача отмечена как выполненная.")
