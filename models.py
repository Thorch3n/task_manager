import json
from datetime import datetime
from typing import Any, Dict, List


class Task:
    def __init__(self, id: int, title: str, description: str, category: str,
                 due_date: str, priority: str, status: str = "Не выполнена"):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
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
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def add_task(self, title, description, category, due_date, priority):
        new_id = max([task.id for task in self.tasks], default=0) + 1
        task = Task(new_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_id: int):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def find_tasks(self, keyword: str = "", category: str = "", status: str = "") -> List[Task]:
        return [
            task for task in self.tasks
            if (keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower())
            and (category == "" or task.category == category)
            and (status == "" or task.status == status)
        ]

    def edit_task(self, task_id: int, title=None, description=None, category=None, due_date=None, priority=None):
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