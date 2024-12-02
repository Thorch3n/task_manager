from models import TaskManager
from handlers import add_task, edit_task, delete_task, complete_task, search_tasks, view_tasks
from typing import Callable, Dict


def main() -> None:
    """
    Главная функция, которая запускает менеджер задач.

    Инициализирует экземпляр TaskManager и предлагает пользователю выбрать одно из действий.
    """
    manager = TaskManager('data.json')

    actions: Dict[str, Callable[[], None]] = {
        '1': lambda: view_tasks.view_tasks(manager),
        '2': lambda: view_tasks.view_tasks_by_category(manager),
        '3': lambda: add_task.add_task(manager),
        '4': lambda: edit_task.edit_task(manager),
        '5': lambda: complete_task.complete_task(manager),
        '6': lambda: delete_task.delete_task(manager),
        '7': lambda: search_tasks.search_tasks(manager),
        '8': lambda: break_program()  # Простой выход с break
    }

    while True:
        # Отображение меню
        print(
            f"\nМенеджер задач:\n"
            f"1. Просмотреть все задачи\n"
            f"2. Просмотреть задачи по категории\n"
            f"3. Добавить задачу\n"
            f"4. Редактировать задачу\n"
            f"5. Отметить задачу как выполненную\n"
            f"6. Удалить задачу\n"
            f"7. Поиск задач\n"
            f"8. Выход\n"
        )

        # Получаем выбор пользователя
        choice: str = input("Выберите действие: ").strip()

        # Выполняем соответствующее действие, если выбор существует в словаре
        action = actions.get(choice)
        if action:
            action()
        else:
            print(f"\nНеверный выбор, попробуйте снова.")


def break_program() -> None:
    """Выход из программы с помощью break."""
    print("\nВыход из программы.")
    raise SystemExit


if __name__ == "__main__":
    main()
