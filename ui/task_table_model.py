from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtCore import QModelIndex


class TaskTableModel(QAbstractTableModel):
    def __init__(self, service):
        super().__init__()
        self._service = service
        self._headers = ["Name", "Priority", "Date"]
        self.tasks = self._service.get_all()

    def set_tasks(self, tasks):
        self.beginResetModel()
        self.tasks = tasks
        self.endResetModel()

    # обновление кеша
    def refresh(self):
        self.set_tasks(self._service.get_all())

    # количество строк
    def rowCount(self, parent=QModelIndex()):
        return len(self.tasks)

    # количество колонок
    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    # данные в ячейках
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            task = self.tasks[index.row()]

            column = index.column()

            if column == 0:
                return task.name
            elif column == 1:
                return task.priority
            elif column == 2:
                return task.date

        return None

    # заголовки таблицы
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
        return None
