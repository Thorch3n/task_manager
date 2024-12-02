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
