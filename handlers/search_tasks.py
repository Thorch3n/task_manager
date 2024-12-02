def search_tasks(manager: "TaskManager") -> None:
    """
    Функция для поиска задач по ключевому слову, категории и статусу.

    :param manager: Экземпляр класса TaskManager, который управляет списком задач.
    """
    # Получение параметров поиска от пользователя
    keyword: str = input("\nВведите ключевое слово для поиска: ").strip()
    category: str = input("Категория (оставьте пустым для всех категорий): ").strip()
    status: str = input("Статус (выполнена/не выполнена, оставьте пустым для всех): ").strip().lower()

    # Получение задач, соответствующих критериям поиска
    tasks = manager.find_tasks(keyword, category, status)

    # Вывод результата поиска
    if not tasks:
        print("\nЗадачи не найдены.")
    else:
        print("\nНайденные задачи:")
        for task in tasks:
            # Преобразование задачи в словарь и вывод
            print(f"- {task.to_dict()}")
