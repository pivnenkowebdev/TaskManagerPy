from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableView,
)

from storage.json_storage import JsonStorage
from services.task_service import TaskService
from ui.task_table_model import TaskTableModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager")
        self.resize(800, 400)

        # --- backend ---
        self.storage = JsonStorage("tasks.json")
        self.service = TaskService(self.storage)

        # --- model ---
        self.model = TaskTableModel(self.service)

        # --- UI ---
        self.table = QTableView()
        self.table.setModel(self.model)

        self.add_button = QPushButton("Добавить задачу")
        self.add_button.clicked.connect(self.add_task)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # --- логика ---
    def add_task(self):
        self.service.add_task("Test Task", "High", "2026-01-01")
        self.model.refresh()