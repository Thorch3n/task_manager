from utils import input_with_validation, validate_non_empty, validate_date_format, validate_priority


def edit_task(manager):
    try:
        task_id = int(input("\nВведите ID задачи для редактирования: "))
    except ValueError:
        print("\nОшибка: ID задачи должен быть числом.")
        return

    task = next((task for task in manager.tasks if task.id == task_id), None)
    if not task:
        print(f"\nЗадача с ID {task_id} не найдена.")
        return
    print('\nПримечание: Если поле не имеет будет меняться, то оставьте строку пустой')
    title = input_with_validation(
        prompt=f"Название ({task.title}): ",
        error_message="",
        validation_func=lambda x: True  # Пропускаем валидацию, пустой ввод допустим
    ).strip()
    if title:
        task.title = title

    description = input_with_validation(
        prompt=f"Описание ({task.description}): ",
        error_message="",
        validation_func=lambda x: True
    ).strip()
    if description:
        task.description = description

    category = input_with_validation(
        prompt=f"Категория ({task.category}): ",
        error_message="",
        validation_func=lambda x: True
    ).strip()
    if category:
        task.category = category

    due_date = input_with_validation(
        prompt=f"Срок ({task.due_date}): ",
        error_message="Ошибка: Некорректный формат даты. Введите дату в формате дд-мм-гггг.",
        validation_func=lambda x: validate_date_format(x, "%d-%m-%Y") if x else True
    ).strip()
    if due_date:
        task.due_date = due_date

    priority = input_with_validation(
        prompt=f"Приоритет ({task.priority}): ",
        error_message="Ошибка: Введите 1, 2, 3 или оставьте пустым.",
        validation_func=lambda x: validate_priority(x) if x else True
    ).strip()
    if priority:
        priority_map = {"1": "Низкий", "2": "Средний", "3": "Высокий"}
        task.priority = priority_map.get(priority, task.priority)

    manager.save_tasks()
    print("\nЗадача обновлена.")
