from PySide6.QtWidgets import (
    QAbstractItemView,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableView,
    QMessageBox
)

from storage.json_storage import JsonStorage
from services.task_service import TaskService
from ui.task_table_model import TaskTableModel
from ui.add_task_dialog import AddTaskDialog

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

        # удаление
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.add_button = QPushButton("Добавить задачу")
        self.add_button.clicked.connect(self.add_task)

        # удаление
        self.delete_button = QPushButton("Удалить задачу")
        self.delete_button.clicked.connect(self.delete_task)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # --- логика ---
    # def add_task(self):
    #     self.service.add_task("Test Task", "High", "2026-01-01")
    #     self.model.refresh()

    def add_task(self):
        dialog = AddTaskDialog(self)

        if dialog.exec():  # если нажали "Добавить"
            name, priority, date = dialog.get_data()

            self.service.add_task(name, priority, date)
            self.model.refresh()

    def delete_task(self):
        selection = self.table.selectionModel().selectedRows()

        if not selection:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу")
            return

        row = selection[0].row()

        # получаем задачу из модели
        task = self.model.tasks[row]

        reply = QMessageBox.question(
            self,
            "Подтверждение",
            f"Удалить задачу '{task.name}'?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.service.delete_task(task.id)
            self.model.refresh()