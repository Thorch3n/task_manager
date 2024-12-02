from utils import input_with_validation, validate_non_empty, validate_date_format, validate_priority


def add_task(manager):
    title = input_with_validation(
        prompt="\nНазвание: ",
        error_message="Ошибка: Название не может быть пустым.",
        validation_func=validate_non_empty
    )

    description = input_with_validation(
        prompt="Описание: ",
        error_message="Ошибка: Описание не может быть пустым.",
        validation_func=validate_non_empty
    )

    category = input_with_validation(
        prompt="Категория: ",
        error_message="Ошибка: Категория не может быть пустой.",
        validation_func=validate_non_empty
    )

    due_date = input_with_validation(
        prompt="Срок (дд-мм-гггг): ",
        error_message="Ошибка: Некорректный формат даты. Введите дату в формате дд-мм-гггг.",
        validation_func=lambda x: validate_date_format(x, "%d-%m-%Y")
    )

    priority = input_with_validation(
        prompt="Приоритет (1 - Низкий, 2 - Средний, 3 - Высокий): ",
        error_message="Ошибка: Введите 1, 2 или 3.",
        validation_func=validate_priority
    )

    priority_map = {"1": "Низкий", "2": "Средний", "3": "Высокий"}
    manager.add_task(title, description, category, due_date, priority_map[priority])
    print("\nЗадача добавлена!")
