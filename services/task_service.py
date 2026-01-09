from models.task import Task


class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self.tasks: list[Task] = self.storage.load()

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        self.storage.save(self.tasks)

    def remove_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.storage.save(self.tasks)
            return True
        return False

    def edit_task(
        self,
        index: int,
        name: str | None = None,
        priority: str | None = None,
        date: str | None = None,
    ) -> bool:
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if name:
                task.name = name
            if priority:
                task.priority = priority
            if date:
                task.date = date
            self.storage.save(self.tasks)
            return True
        return False

    def search(self, keyword: str) -> list[Task]:
        keyword = keyword.lower()
        return [
            task
            for task in self.tasks
            if keyword in task.name.lower()
        ]

    def get_all(self) -> list[Task]:
        return self.tasks
