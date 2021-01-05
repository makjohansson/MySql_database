from PyQt5.QtWidgets import QDial, QDialog, QMainWindow, QPushButton, QStackedLayout, QStackedWidget, QTableView
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QApplication
from PyQt5.QtCore import Qt
import sys

from PyQt5 import QtCore


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self.data = data
        self.header_labels = ["Name", "Category", "Contact", "Phone number", "Mail", "Joined", "Employee"]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()][index.column()]
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
    
    def rowCount(self, index):
        return len(self.data)
    
    def columnCount(self, index):
        return len(self.data[0])


class TestLabel(QLabel, QWidget):
    def __init__(self, label):
        super(TestLabel, self).__init__()
        self.label = label
        self.set_background()
        self.set_label()
       
    def set_background(self):
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(43, 47, 59))
        self.setPalette(palette)
    
    def set_label(self):
        self.setText(self.label)
        self.setAlignment(Qt.AlignHCenter)
        font = self.font()
        font.setPointSize(30)
        font.setBold(True)
        self.setStyleSheet('color: rgb(245,245,245);')
        self.setFont(font)

        


class MainWindow(QMainWindow):

    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Guldhäftet")
        self.setGeometry(300, 200, 800, 500)

        self.titles = ['Company', 'Association', 'Stats', 'Employess']
        main_layout = QHBoxLayout()
        btn_layout = QVBoxLayout()

        # Widget stack for the tab like gui
        self.stack_one = QWidget()
        self.stack_two = QWidget()
        self.stack_three= QWidget()
        self.stack_four = QWidget()

        # First tab gui
        self.stack_oneUI()
        self.stack_twoUI()
        self.stack_threeUI()
        self.stack_fourUI()

        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack_one)
        self.stack.addWidget(self.stack_two)
        self.stack.addWidget(self.stack_three)
        self.stack.addWidget(self.stack_four)

        
        main_layout.addLayout(btn_layout)

        main_layout.addWidget(self.stack)

        
        company_btn = QPushButton(self.titles[0])
        company_btn.pressed.connect(self.btn_company)
        btn_layout.addWidget(company_btn)
        
        ass_btn = QPushButton(self.titles[1])
        ass_btn.pressed.connect(self.btn_association)
        btn_layout.addWidget(ass_btn)

        inProg_btn = QPushButton(self.titles[2])
        inProg_btn.pressed.connect(self.btn_inProgress)
        btn_layout.addWidget(inProg_btn)

        emp_btn = QPushButton(self.titles[3])
        emp_btn.pressed.connect(self.btn_employees)
        btn_layout.addWidget(emp_btn)

        btn_layout.setAlignment(QtCore.Qt.AlignTop)

        
        
        widget = QWidget()
        widget.setLayout(main_layout)
        
        self.setCentralWidget(widget)
    
    def btn_company(self):
        self.stack.setCurrentIndex(0)
    
    def btn_association(self):
        self.stack.setCurrentIndex(1)

    def btn_inProgress(self):
        self.stack.setCurrentIndex(2)
    
    def btn_employees(self):
        self.stack.setCurrentIndex(3)
    
    def stack_oneUI(self):
        container = QVBoxLayout()
        table = self.setup_table()
        container.addWidget(TestLabel(self.titles[0]))
        container.addWidget(table)
        self.stack_one.setLayout(container)
    
    def stack_twoUI(self):
        container = QVBoxLayout()
        table = self.setup_table()
        container.addWidget(TestLabel(self.titles[1]))
        container.addWidget(table)
        self.stack_two.setLayout(container)
    
    def stack_threeUI(self):
        container = QVBoxLayout()
        table = self.setup_table()
        container.addWidget(TestLabel(self.titles[2]))
        container.addWidget(table)
        self.stack_three.setLayout(container)
    
    def stack_fourUI(self):
        container = QVBoxLayout()
        table = self.setup_table()
        container.addWidget(TestLabel(self.titles[3]))
        container.addWidget(table)
        self.stack_four.setLayout(container)
    
    def setup_table(self):
        data = [
          [4, 9, 2, 5, 6, 1, 7],
          [1, 0, 0, 5, 6, 1, 7],
          [3, 5, 0, 5, 6, 0, 7],
          [3, 3, 2, 5, 6, 1, 7],
          [7, 8, 9, 5, 6, 0, 7],
        ]
        table = QTableView()
        self.model = TableModel(data)
        table.setModel(self.model)
        table.setShowGrid(False)
        table.clicked.connect(self.first_test)
        table.setStyleSheet("QTableView::item {border-bottom: 1px solid #d6d9dc;} QTableView {background: #2b2f3b; color: #f5f5f5; }")

        return table

    def first_test(self, i):
        cell = i.data()
        dlg = QDialog(self)
        s = f"Row {i.row()}, Col {i.column()}"
        dlg.setWindowTitle(s)
        label = QLabel(dlg)
        label.setText(self.print_model(i.row()))
        label.move(80, 100)
        
        dlg.exec_()
    
    def print_model(self, row):
        s = ""
        for col in range(self.model.columnCount(row)):
            index = self.model.index(row, col)
            s += str(index.data()) + ", "
            print(index.data(), end=', ')
        print()
        return s
        



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()