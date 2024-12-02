from datetime import datetime


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
