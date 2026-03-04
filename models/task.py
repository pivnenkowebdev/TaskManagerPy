class Task:
    def __init__(self, id: int, name: str, priority: str, date: str):
        self.id = id
        self.name = name
        self.priority = priority
        self.date = date

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "priority": self.priority,
            "date": self.date,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            id=data["id"],
            name=data["name"],
            priority=data["priority"],
            date=data["date"],
        )