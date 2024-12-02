from datetime import datetime


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