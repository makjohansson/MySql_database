from view.tablemodel import TableModel
from model import db_connector
from PyQt5.QtWidgets import QDialog, QGridLayout, QMainWindow, QPushButton, QStackedWidget, QTableView
from PyQt5.QtGui import QColor, QPalette, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from controller import DatabaseController


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Guldhäftet")
        self.setGeometry(300, 200, 1030, 600)
        self.db_controller = DatabaseController()

        # Tab titles
        self.titles = ['Companies', 'Associations', 'Stats', 'Employess']

        # Main and btn layout
        main_layout = QHBoxLayout()
        btn_layout = QVBoxLayout()

        # Widget stack for the tab-like gui
        self.stack_one = QWidget()
        self.stack_two = QWidget()
        self.stack_three = QWidget()
        self.stack_four = QWidget()

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

        btn_layout.setAlignment(Qt.AlignTop)

        widget = QWidget()
        widget.setLayout(main_layout)
        widget.setAutoFillBackground(True)
        palette = widget.palette()
        palette.setColor(QPalette.Window, QColor(245, 245, 245))
        widget.setPalette(palette)

        self.setCentralWidget(widget)

    def btn_company(self):
        self.stack.setCurrentIndex(0)

    def btn_association(self):
        self.stack.setCurrentIndex(1)

    def btn_inProgress(self):
        self.stack.setCurrentIndex(2)

    def btn_employees(self):
        self.stack.setCurrentIndex(3)

    def tab_label(self, title):
        label = QLabel(title)
        label.setMaximumHeight(50)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            'color: rgb(54, 54, 54); font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 30px;')
        return label
    
    

    def stack_oneUI(self):
        container = QVBoxLayout()
        header_labels = ["Name", "Category", "Contact",
                         "Phone number", "Mail", "Joined", "Employee", "Id"]
        data = self.db_controller.fill_company_table()
        table = self.setup_table(data, header_labels)
        container.addWidget(self.tab_label(self.titles[0]))
        container.addWidget(table)
        self.stack_one.setLayout(container)

    def stack_twoUI(self):
        container = QVBoxLayout()
        header_labels = ["Name", "Category", "Contact",
                         "Phone number", "Mail", "Joined", "Employee", "Id"]
        data = self.db_controller.fill_association_table()
        data = [data]
        table = self.setup_table(data, header_labels)
        container.addWidget(self.tab_label(self.titles[1]))
        container.addWidget(table)
        self.stack_two.setLayout(container)

    def stack_threeUI(self):
        container = QVBoxLayout()
        header_labels = ["Name", "Category", "Contact",
                         "Phone number", "Mail", "Joined", "Employee", "Id"]
        data = self.db_controller.fill_company_table()
        table = self.setup_table(data, header_labels)
        container.addWidget(self.tab_label(self.titles[2]))
        container.addWidget(table)
        self.stack_three.setLayout(container)

    def employee_grid(self):
        grid = QVBoxLayout()
        row_one = QHBoxLayout()
        row_two = QHBoxLayout()
        
        QLabels = self.fill_grid()
        pixmap = QPixmap('view/img/avatar.png')
        pixmap_girl = QPixmap('view/img/avatar_girl.png')

        label = QLabel()
        label.setPixmap(pixmap)
        label.setMaximumSize(pixmap.width(), pixmap.height())
        row_one.addWidget(label)
        row_one.addWidget(QLabels[0])

        label = QLabel()
        label.setPixmap(pixmap_girl)
        label.setMaximumSize(pixmap_girl.width(), pixmap_girl.height())
        row_one.addWidget(label)
        row_one.addWidget(QLabels[1])
        
        label = QLabel()
        label.setPixmap(pixmap_girl)
        label.setMaximumSize(pixmap_girl.width(), pixmap_girl.height())
        row_two.addWidget(label)
        row_two.addWidget(QLabels[2])

        label = QLabel()
        label.setPixmap(pixmap_girl)
        label.setMaximumSize(pixmap_girl.width(), pixmap_girl.height())
        row_two.addWidget(label)
        row_two.addWidget(QLabels[3])
        
        grid.addLayout(row_one)
        grid.addLayout(row_two)
        widget = QWidget()
        widget.setLayout(grid)
        return widget
    
    def fill_grid(self):
        QLabels = []
        emp_info = ""
        data = self.db_controller.employee_info()
    
        for row in range(len(data)):
            count = self.db_controller.employees_company_count(data[row][0])
            role = "Manager" if data[row][2] == None else "Sales" 
            emp_info = f"Name: {data[row][1]}\nRole: {role}\nApp-code's sold: {data[row][3]}\nCompanies: {count}"
            label = QLabel(emp_info)
            label.setStyleSheet("""
                color: rgb(54, 54, 54);
                font-family: Arial, Helvetica, sans-serif;
                font-size: 15px;
            """)
            QLabels.append(label)
        return QLabels
            
    def stack_fourUI(self):
        container = QVBoxLayout()
        container.addWidget(self.tab_label(self.titles[3]))

        container.addWidget(self.employee_grid())
        self.stack_four.setLayout(container)

    def setup_table(self, data, header_labels):
        table = QTableView()
        self.model = TableModel(data, header_labels)
        table.setModel(self.model)
        # table.resizeColumnsToContents()
        #table.setMaximumSize(720, 300)
        table.setShowGrid(False)
        table.clicked.connect(self.first_test)
        table.setStyleSheet(
            "QTableView::item {border-bottom: 1px solid #d6d9dc;} QTableView {background: #2b2f3b; color: #f5f5f5; }")

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
