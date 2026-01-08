import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget,
    QPushButton, QVBoxLayout, QWidget
)
from storage import load_tasks, save_tasks

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager")

        self.tasks = load_tasks()

        self.list_widget = QListWidget()
        self.refresh_list()

        self.add_btn = QPushButton("Добавить")
        self.add_btn.clicked.connect(self.add_task)

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def refresh_list(self):
        self.list_widget.clear()
        for task in self.tasks:
            self.list_widget.addItem(
                f"{task['name']} | {task['priority']} | {task['date']}"
            )

    def add_task(self):
        # пока заглушка
        self.tasks.append({
            "name": "Тест",
            "priority": "средний",
            "date": "2026-01-01"
        })
        save_tasks(self.tasks)
        self.refresh_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
