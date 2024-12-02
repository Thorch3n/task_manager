import json
from datetime import datetime
from typing import Any, Dict, List


class Task:
    """
    Класс, представляющий задачу.

    Атрибуты:
    - id: int — уникальный идентификатор задачи.
    - title: str — название задачи.
    - description: str — описание задачи.
    - category: str — категория задачи.
    - due_date: str — срок выполнения задачи (формат дд-мм-гггг).
    - priority: str — приоритет задачи ("Низкий", "Средний", "Высокий").
    - status: str — статус задачи ("Не выполнена" по умолчанию).
    """

    def __init__(self, id: int, title: str, description: str, category: str,
                 due_date: str, priority: str, status: str = "Не выполнена"):
        """
        Конструктор для создания новой задачи.

        :param id: Уникальный идентификатор задачи.
        :param title: Название задачи.
        :param description: Описание задачи.
        :param category: Категория задачи.
        :param due_date: Срок выполнения задачи.
        :param priority: Приоритет задачи.
        :param status: Статус задачи (по умолчанию "Не выполнена").
        """
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразует задачу в словарь для сохранения.

        :return: Словарь, содержащий атрибуты задачи.
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": self.due_date,
            "priority": self.priority,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Task':
        """
        Создает экземпляр задачи из словаря.

        :param data: Словарь, содержащий данные задачи.
        :return: Экземпляр задачи.
        """
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            category=data["category"],
            due_date=data["due_date"],
            priority=data["priority"],
            status=data["status"]
        )


class TaskManager:
    """
    Класс для управления списком задач.

    Атрибуты:
    - file_path: str — путь к файлу, в котором хранятся задачи.
    - tasks: List[Task] — список задач.
    """

    def __init__(self, file_path: str):
        """
        Конструктор для инициализации менеджера задач.

        :param file_path: Путь к файлу, в котором будут храниться задачи.
        """
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        """
        Загружает задачи из файла.

        :return: Список задач.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            return []

    def save_tasks(self) -> None:
        """
        Сохраняет задачи в файл.

        :return: None
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str) -> None:
        """
        Добавляет новую задачу в список задач.

        :param title: Название задачи.
        :param description: Описание задачи.
        :param category: Категория задачи.
        :param due_date: Срок выполнения задачи.
        :param priority: Приоритет задачи.
        :return: None
        """
        new_id = max([task.id for task in self.tasks], default=0) + 1
        task = Task(new_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_id: int) -> None:
        """
        Удаляет задачу по ее идентификатору.

        :param task_id: Идентификатор задачи, которую необходимо удалить.
        :return: None
        """
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def find_tasks(self, keyword: str = "", category: str = "", status: str = "") -> List[Task]:
        """
        Находит задачи по ключевому слову, категории и статусу.

        :param keyword: Ключевое слово для поиска в названии и описании задачи.
        :param category: Категория для фильтрации задач.
        :param status: Статус задачи ("выполнена" или "не выполнена").
        :return: Список задач, соответствующих критериям поиска.
        """
        status = status.strip().lower()
        return [
            task for task in self.tasks
            if (
                           keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower())
               and (category == "" or category.lower() == task.category.lower())
               and (status == "" or (status == "выполнена" and task.status == "Выполнена") or (
                    status == "не выполнена" and task.status != "Выполнена"))
        ]

    def edit_task(self, task_id: int, title: str = None, description: str = None, category: str = None,
                  due_date: str = None, priority: str = None) -> None:
        """
        Редактирует существующую задачу по ее идентификатору.

        :param task_id: Идентификатор задачи, которую нужно отредактировать.
        :param title: Новое название задачи (если передано).
        :param description: Новое описание задачи (если передано).
        :param category: Новая категория задачи (если передано).
        :param due_date: Новый срок выполнения задачи (если передан).
        :param priority: Новый приоритет задачи (если передан).
        :return: None
        :raises: ValueError, если задача не найдена или дата имеет неверный формат.
        """
        task = next((task for task in self.tasks if task.id == task_id), None)
        if not task:
            raise ValueError(f"Задача с ID {task_id} не найдена.")

        # Обновляем поля, если они были переданы
        if title:
            task.title = title
        if description:
            task.description = description
        if category:
            task.category = category
        if due_date:
            try:
                # Проверка формата даты
                datetime.strptime(due_date, "%d-%m-%Y")
                task.due_date = due_date
            except ValueError:
                raise ValueError("Некорректный формат даты. Введите дату в формате дд-мм-гггг.")
        if priority:
            task.priority = priority

        self.save_tasks()
