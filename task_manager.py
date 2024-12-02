from models import TaskManager
from datetime import datetime


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
            view_tasks(manager)
        elif choice == '2':
            view_tasks_by_category(manager)
        elif choice == '3':
            add_task(manager)
        elif choice == '4':
            edit_task(manager)
        elif choice == '5':
            complete_task(manager)
        elif choice == '6':
            delete_task(manager)
        elif choice == '7':
            search_tasks(manager)
        elif choice == '8':
            break
        else:
            print(f"\nНеверный выбор, попробуйте снова.")


def view_tasks(manager):
    tasks = manager.tasks
    if not tasks:
        print(f"\nСписок задач пуст.")
    else:
        for task in tasks:
            print(f"\n{task.to_dict()}")


def view_tasks_by_category(manager):
    category = input(f"\nВведите категорию: ")
    tasks = [task for task in manager.tasks if task.category == category]
    if not tasks:
        print(f"\nНет задач в категории '{category}'.")
    else:
        for task in tasks:
            print(f"\n{task.to_dict()}")


def add_task(manager):
    while True:
        title = input(f"\nНазвание: ").strip()
        if not title:
            print("\nОшибка: Название не может быть пустым.")
            continue
        break

    while True:
        description = input(f"Описание: ").strip()
        if not description:
            print("\nОшибка: Описание не может быть пустым.")
            continue
        break

    while True:
        category = input(f"Категория: ").strip()
        if not category:
            print("\nОшибка: Категория не может быть пустой.")
            continue
        break

    while True:
        due_date = input(f"Срок (дд-мм-гггг): ").strip()
        try:
            # Проверка формата даты
            datetime.strptime(due_date, "%d-%m-%Y")
            break
        except ValueError:
            raise ValueError(f"\nОшибка: Некорректный формат даты. Введите дату в формате дд-мм-гггг.")

    while True:
        priority = input(f"Приоритет (1 - Низкий, 2 - Средний, 3 - Высокий): ").strip()
        if priority == '1':
            priority = "Низкий"
            break
        elif priority == '2':
            priority = "Средний"
            break
        elif priority == '3':
            priority = "Высокий"
            break
        else:
            print(f"\nОшибка: Введите 1, 2 или 3.")

    manager.add_task(title, description, category, due_date, priority)
    print(f"\nЗадача добавлена!")


def edit_task(manager):
    try:
        task_id = int(input(f"\nВведите ID задачи для редактирования: "))
    except ValueError:
        print(f"\nОшибка: ID задачи должен быть числом.")
        return

    task = next((task for task in manager.tasks if task.id == task_id), None)
    if not task:
        print(f"\nЗадача с ID {task_id} не найдена.")
        return

    while True:
        title = input(f"Название ({task.title}): ").strip()
        if title:  # Если введено новое значение, то обновим
            task.title = title
        break

    while True:
        description = input(f"Описание ({task.description}): ").strip()
        if description:
            task.description = description
        break

    while True:
        category = input(f"Категория ({task.category}): ").strip()
        if category:
            task.category = category
        break

    while True:
        due_date = input(f"Срок ({task.due_date}): ").strip()
        if due_date:
            try:
                # Проверка формата даты
                datetime.strptime(due_date, "%d-%m-%Y")
                task.due_date = due_date
                break
            except ValueError:
                raise ValueError(f"\nОшибка: Некорректный формат даты. Введите дату в формате дд-мм-гггг.")
        else:
            break

    while True:
        priority = input(f"Приоритет ({task.priority}): ").strip()
        if priority:
            if priority in ['1', '2', '3']:
                task.priority = {"1": "Низкий", "2": "Средний", "3": "Высокий"}[priority]
                break
            elif priority in ["Низкий", "Средний", "Высокий"]:
                task.priority = priority
                break
            else:
                print(f"\nОшибка: Введите 1, 2 или 3.")
        else:
            break

    manager.save_tasks()
    print(f"\nЗадача обновлена.")


def complete_task(manager):
    try:
        task_id = int(input(f"\nВведите ID выполненной задачи: "))
    except ValueError:
        print(f"\nОшибка: ID задачи должен быть числом.")
        return

    task = next((task for task in manager.tasks if task.id == task_id), None)
    if not task:
        print(f"\nЗадача с ID {task_id} не найдена.")
        return

    task.status = "Выполнена"
    manager.save_tasks()
    print(f"\nЗадача отмечена как выполненная.")


def delete_task(manager):
    choice = input("\nВыберите, как удалить задачу:\n"
                   "1. По идентификатору\n"
                   "2. По категории\n"
                   "Введите ваш выбор: ").strip()

    if choice == '1':
        try:
            task_id = int(input(f"\nВведите ID задачи для удаления: "))
        except ValueError:
            print(f"\nОшибка: ID задачи должен быть числом.")
            return

        task = next((task for task in manager.tasks if task.id == task_id), None)
        if not task:
            print(f"\nЗадача с ID {task_id} не найдена.")
        else:
            manager.delete_task(task_id)
            print(f"\nЗадача с ID {task_id} удалена.")

    elif choice == '2':
        category = input(f"\nВведите категорию задач для удаления: ").strip()
        tasks_to_delete = [task for task in manager.tasks if task.category.lower() == category.lower()]

        if not tasks_to_delete:
            print(f"\nЗадачи в категории '{category}' не найдены.")
        else:
            for task in tasks_to_delete:
                manager.delete_task(task.id)
            print(f"\nЗадачи в категории '{category}' удалены.")

    else:
        print("\nОшибка: Неверный выбор.")


def search_tasks(manager):
    keyword = input(f"\nВведите ключевое слово для поиска: ")
    category = input(f"Категория (оставьте пустым для всех категорий): ")
    status = input(f"Статус (выполнена/не выполнена, оставьте пустым для всех): ")
    tasks = manager.find_tasks(keyword, category, status)
    if not tasks:
        print(f"\nЗадачи не найдены.")
    else:
        for task in tasks:
            print(f"\n{task.to_dict()}")


if __name__ == "__main__":
    main()
