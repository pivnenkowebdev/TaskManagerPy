import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

from storage.json_storage import JsonStorage
from services.task_service import TaskService
from ui.task_table_model import TaskTableModel


def main():
    app = QApplication(sys.argv)

    storage = JsonStorage("tasks.json")
    service = TaskService(storage)

    window = QMainWindow()
    table = QTableView()

    model = TaskTableModel(service)
    table.setModel(model)

    window.setCentralWidget(table)
    window.resize(800, 400)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

# import sys
# from PySide6.QtWidgets import QApplication
# from ui.main_window import MainWindow


# def main():
#     app = QApplication(sys.argv)

#     window = MainWindow()
#     window.show()

#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()