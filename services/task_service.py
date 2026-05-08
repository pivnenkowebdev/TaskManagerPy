from models.task import Task

class TaskService:
    def __init__(self, storage):
        self.storage = storage
        self.tasks: list[Task] = self.storage.load()
        self._next_id = max((task.id for task in self.tasks), default=0) + 1


    def add_task(self, name: str, priority: str, date: str) -> Task:
        if not name.strip():
            raise ValueError("Task name cannot be empty.")

        task = Task(
            id=self._next_id,
            name=name,
            priority=priority,
            date=date,
        )

        self._next_id += 1
        self.tasks.append(task)
        self.storage.save(self.tasks)

        return task
    
    def search(self, keyword: str):
        keyword = keyword.lower()

        return [
            task
            for task in self.tasks
            if keyword in task.name.lower()
        ]

    def get_all(self) -> list[Task]:
        return list(self.tasks)

    def get_task(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(
        self,
        task_id: int,
        name: str,
        priority: str,
        date: str,
    ) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False

        if not name.strip():
            raise ValueError("Task name cannot be empty.")

        task.name = name
        task.priority = priority
        task.date = date

        self.storage.save(self.tasks)
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        self.storage.save(self.tasks)
        return True
    