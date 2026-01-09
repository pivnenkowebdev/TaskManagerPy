from storage.json_storage import JsonStorage
from services.task_service import TaskService
from ui.console_ui import ConsoleUI

file_name = "tasks.json"

def main():
    storage = JsonStorage(filename=file_name)
    service = TaskService(storage)
    ui = ConsoleUI(service)
    ui.run()

if __name__ == "__main__":
    main()
