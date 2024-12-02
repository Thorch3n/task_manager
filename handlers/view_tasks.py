def view_tasks(manager):
    tasks = manager.tasks
    if not tasks:
        print(f"\nСписок задач пуст.")
    else:
        for task in tasks:
            print(f"\n{task.to_dict()}")