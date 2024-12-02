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