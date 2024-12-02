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