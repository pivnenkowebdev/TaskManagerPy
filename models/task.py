class Task:
    def __init__(self, name: str, priority: str, date: str):
        self.name = name
        self.priority = priority
        self.date = date

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "priority": self.priority,
            "date": self.date,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            name=data["name"],
            priority=data["priority"],
            date=data["date"],
        )
