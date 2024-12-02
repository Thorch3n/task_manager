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