import json
from models.task import Task

class JsonStorage:
    def __init__(self, filename: str):
        self.filename = filename

    def load(self) -> list[Task]:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self, tasks: list[Task]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [task.to_dict() for task in tasks],
                f,
                ensure_ascii=False,
                indent=4,
            )
