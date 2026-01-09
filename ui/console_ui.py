from models.task import Task

class ConsoleUI:
    def __init__(self, service):
        self.service = service

    def run(self):
        while True:
            print("\nМеню:")
            print("1 — добавить задачу")
            print("2 — удалить задачу")
            print("3 — редактировать задачу")
            print("4 — показать все задачи")
            print("5 — поиск")
            print("0 — выход")

            choice = input("Выбор: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.remove_task()
            elif choice == "3":
                self.edit_task()
            elif choice == "4":
                self.show_tasks()
            elif choice == "5":
                self.search_tasks()
            elif choice == "0":
                print("Выход.")
                break
            else:
                print("Неверный выбор.")

    def add_task(self):
        name = input("Название: ")
        priority = input("Приоритет: ")
        date = input("Дата (ГГГГ-ММ-ДД): ")

        task = Task(name, priority, date)
        self.service.add_task(task)
        print("Задача добавлена.")

    def remove_task(self):
        self.show_tasks()
        try:
            index = int(input("Номер задачи: ")) - 1
            if self.service.remove_task(index):
                print("Задача удалена.")
            else:
                print("Неверный номер.")
        except ValueError:
            print("Ошибка ввода.")

    def edit_task(self):
        self.show_tasks()
        try:
            index = int(input("Номер задачи: ")) - 1
        except ValueError:
            print("Ошибка.")
            return

        name = input("Новое название (Enter — пропустить): ")
        priority = input("Новый приоритет (Enter — пропустить): ")
        date = input("Новая дата (Enter — пропустить): ")

        success = self.service.edit_task(
            index,
            name=name or None,
            priority=priority or None,
            date=date or None,
        )

        if success:
            print("Задача обновлена.")
        else:
            print("Ошибка редактирования.")

    def show_tasks(self):
        tasks = self.service.get_all()
        if not tasks:
            print("Задач нет.")
            return

        print("\nСписок задач:")
        for i, task in enumerate(tasks, start=1):
            print(
                f"{i}. {task.name} | "
                f"{task.priority} | "
                f"{task.date}"
            )

    def search_tasks(self):
        keyword = input("Поиск: ")
        results = self.service.search(keyword)

        if not results:
            print("Ничего не найдено.")
            return

        print("Найдено:")
        for task in results:
            print(
                f"- {task.name} | "
                f"{task.priority} | "
                f"{task.date}"
            )
