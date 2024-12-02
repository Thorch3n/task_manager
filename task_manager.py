from models import TaskManager
from datetime import datetime
from handlers import add_task, edit_task, delete_task, complete_task, search_tasks, view_tasks

def main():
    manager = TaskManager('data.json')

    while True:
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

        choice = input("Выберите действие: ")

        if choice == '1':
            view_tasks.view_tasks(manager)
        elif choice == '2':
            view_tasks.view_tasks_by_category(manager)
        elif choice == '3':
            add_task.add_task(manager)
        elif choice == '4':
            edit_task.edit_task(manager)
        elif choice == '5':
            complete_task.complete_task(manager)
        elif choice == '6':
            delete_task.delete_task(manager)
        elif choice == '7':
            search_tasks.search_tasks(manager)
        elif choice == '8':
            break
        else:
            print(f"\nНеверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
