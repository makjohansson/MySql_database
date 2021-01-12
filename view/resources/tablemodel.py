from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
    counter = 0
    def __init__(self, data, header_labels, main_tabel=True):
        super(TableModel, self).__init__()
        self.data = data
        self.header_labels = header_labels
        self.main_tabel = main_tabel

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if index.column() == 5 and role == Qt.DisplayRole and self.main_tabel:
            if self.data[index.row()][index.column()] == 1:
                return True
            else:
                return False
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.data[0])