from PySide6.QtCore import QAbstractTableModel, Qt


class TableModel(QAbstractTableModel):
    def __init__(self, *args, hashes: list[list[str]], **kwargs):
        super(TableModel, self).__init__(*args, **kwargs)
        self._data = hashes
        self.column_names = ["File", "Algorithm", "Hash"]

    def data(self, index, role):

        row = index.row()
        column = index.column()
        if not index.isValid() or row >= len(self._data):
            return None

        if role != Qt.DisplayRole and role != Qt.EditRole:
            return None

        return self._data[row][column]

    def rowCount(self, index=None):
        return len(self._data)

    def columnCount(self, index=None) -> int:
        return len(self._data[0])

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:

                if self.columnCount() == 2:
                    return [self.column_names[0], self.column_names[2]][section]

                return self.column_names[section]

    def clear_all(self):
        self._data = [[]]
