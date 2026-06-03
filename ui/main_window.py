from PySide6.QtWidgets import (
    QAbstractItemView,
    QLineEdit,
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

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск...")
        self.search_input.textChanged.connect(self.search_tasks)
        
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

        # изменение
        self.edit_button = QPushButton("Редактировать задачу")
        self.edit_button.clicked.connect(self.edit_task)
        
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.edit_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    # --- логика ---
    # def add_task(self):
    #     self.service.add_task("Test Task", "High", "2026-01-01")
    #     self.model.refresh()

    def edit_task(self):
        selection = self.table.selectionModel().selectedRows()

        if not selection:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберите задачу"
            )
            return

        row = selection[0].row()
        task = self.model.tasks[row]

        dialog = AddTaskDialog(
            self,
            task=task
        )

        if dialog.exec():
            name, priority, date = dialog.get_data()

            self.service.update_task(
                task.id,
                name,
                priority,
                date,
            )

            self.model.refresh()

    def search_tasks(self, text):
        text = text.strip()

        if not text:
            self.model.refresh()
            return

        results = self.service.search(text)
        self.model.set_tasks(results)

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