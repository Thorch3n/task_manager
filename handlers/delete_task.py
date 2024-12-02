from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import TaskManager  # Импортируем только для проверки типов


def delete_task(manager: "TaskManager") -> None:
    """
    Функция для удаления задач из менеджера задач.

    :param manager: Экземпляр класса TaskManager, который управляет списком задач.
    """
    # Запрос выбора способа удаления
    choice: str = input(
        "\nВыберите, как удалить задачу:\n"
        "1. По идентификатору\n"
        "2. По категории\n"
        "Введите ваш выбор: "
    ).strip()

    # Удаление задачи по идентификатору
    if choice == '1':
        try:
            task_id: int = int(input("\nВведите ID задачи для удаления: "))
        except ValueError:
            print("\nОшибка: ID задачи должен быть числом.")
            return

        # Поиск задачи с заданным ID
        task = next((task for task in manager.tasks if task.id == task_id), None)
        if not task:
            print(f"\nЗадача с ID {task_id} не найдена.")
        else:
            manager.delete_task(task_id)  # Удаляем задачу
            print(f"\nЗадача с ID {task_id} удалена.")

    # Удаление задач по категории
    elif choice == '2':
        category: str = input("\nВведите категорию задач для удаления: ").strip()
        tasks_to_delete = [
            task for task in manager.tasks if task.category.lower() == category.lower()
        ]

        if not tasks_to_delete:
            print(f"\nЗадачи в категории '{category}' не найдены.")
        else:
            # Удаляем каждую задачу в выбранной категории
            for task in tasks_to_delete:
                manager.delete_task(task.id)
            print(f"\nЗадачи в категории '{category}' удалены.")

    # Обработка неверного выбора
    else:
        print("\nОшибка: Неверный выбор.")
