import pytest
from models import Task
from datetime import datetime


@pytest.fixture
def task() -> Task:
    """
    Фикстура для создания экземпляра задачи, который будет использоваться в тестах.

    :return: Экземпляр задачи Task с заданными параметрами.
    """
    return Task(1, "Задача 1", "Описание задачи 1", "Работа", "31-12-2024", "Низкий")


def test_task_initialization(task: Task) -> None:
    """
    Тест для проверки правильной инициализации задачи.

    :param task: Экземпляр задачи, переданный через фикстуру.
    """
    assert task.id == 1
    assert task.title == "Задача 1"
    assert task.description == "Описание задачи 1"
    assert task.category == "Работа"
    assert task.due_date == "31-12-2024"
    assert task.priority == "Низкий"
    assert task.status == "Не выполнена"


def test_task_due_date_conversion(task: Task) -> None:
    """
    Тест для проверки правильной конверсии строки даты в объект datetime.

    :param task: Экземпляр задачи, переданный через фикстуру.
    """
    task_due_date = datetime.strptime(task.due_date, "%d-%m-%Y")
    assert task_due_date == datetime(2024, 12, 31)


def test_task_to_dict(task: Task) -> None:
    """
    Тест для проверки метода to_dict у задачи.

    :param task: Экземпляр задачи, переданный через фикстуру.
    """
    task_dict = task.to_dict()
    assert isinstance(task_dict, dict)
    assert task_dict["id"] == task.id
    assert task_dict["title"] == task.title
    assert task_dict["description"] == task.description
    assert task_dict["category"] == task.category
    assert task_dict["due_date"] == task.due_date
    assert task_dict["priority"] == task.priority
    assert task_dict["status"] == task.status


def test_task_from_dict() -> None:
    """
    Тест для проверки метода from_dict у задачи.

    :return: None
    """
    task_data = {
        "id": 2,
        "title": "Задача 2",
        "description": "Описание задачи 2",
        "category": "Дом",
        "due_date": "01-01-2025",
        "priority": "Средний",
        "status": "В процессе"
    }
    task = Task.from_dict(task_data)
    assert task.id == task_data["id"]
    assert task.title == task_data["title"]
    assert task.description == task_data["description"]
    assert task.category == task_data["category"]
    assert task.due_date == task_data["due_date"]
    assert task.priority == task_data["priority"]
    assert task.status == task_data["status"]
