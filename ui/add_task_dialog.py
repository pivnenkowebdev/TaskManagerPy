from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
)
from PySide6.QtCore import QDate


class AddTaskDialog(QDialog):
    def __init__(self, parent=None, task=None):
        super().__init__(parent)

        if task:
            self.setWindowTitle("Редактировать задачу")
        else:
            self.setWindowTitle("Добавить задачу")

        self.setModal(True)
        self.resize(300, 200)

        # --- поля ---
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Название задачи")

        self.priority_input = QComboBox()
        self.priority_input.addItems(["Low", "Medium", "High"])

        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)

        # --- кнопки ---
        if task:
            self.ok_button = QPushButton("Редактировать")
        else:
            self.ok_button = QPushButton("Добавить")
            
        self.cancel_button = QPushButton("Отмена")

        self.ok_button.clicked.connect(self.on_accept)
        self.cancel_button.clicked.connect(self.reject)

        # --- layout ---
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Название"))
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Приоритет"))
        layout.addWidget(self.priority_input)

        layout.addWidget(QLabel("Дата"))
        layout.addWidget(self.date_input)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        layout.addLayout(buttons_layout)

        if task:
            self.name_input.setText(task.name)

            self.priority_input.setCurrentText(
                task.priority
            )

            self.date_input.setDate(
                QDate.fromString(
                    task.date,
                    "yyyy-MM-dd"
                )
            )

        self.setLayout(layout)

    # --- обработка OK ---
    def on_accept(self):
        if not self.name_input.text().strip():
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")
            return

        self.accept()

    # --- получить данные ---
    def get_data(self):
        name = self.name_input.text()
        priority = self.priority_input.currentText()
        date = self.date_input.date().toString("yyyy-MM-dd")

        return name, priority, date