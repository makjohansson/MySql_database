from view.resources.tablemodel import TableModel
from view.resources.employee_view import EmployeeGrid
from PyQt5.QtWidgets import QMainWindow, QPushButton, QStackedWidget, QTableView
from PyQt5.QtGui import QColor, QPalette, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from controller import DatabaseController
from view.resources.company_form_view import CompanyForm


class MainWindow(QMainWindow):
    """The main application layout
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Guldhaftet")
        self.setGeometry(300, 200, 1030, 600)
        self.db_controller = DatabaseController()

        # Tab titles
        self.titles = ['Companies', 'Associations', 'Stats', 'Employees']

        self.gui_setup()

    def gui_setup(self):
        """Setup the stacked view for the main layout of the applicaition
        Gets the data need to present the main view from the database 
        """
        # Main and btn layout
        main_layout = QHBoxLayout()
        btn_layout = QVBoxLayout()

        # Widget stack for the tab-like gui
        self.stack_one = QWidget()
        self.stack_two = QWidget()
        self.stack_three = QWidget()
        self.stack_four = QWidget()

        # The layouts for each tab created
        self.stack_oneUI()
        self.stack_twoUI()
        self.stack_threeUI()
        self.stack_fourUI()

        # Create the QStackedWidget to get a tab like layout
        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack_one)
        self.stack.addWidget(self.stack_two)
        self.stack.addWidget(self.stack_three)
        self.stack.addWidget(self.stack_four)

        main_layout.addLayout(btn_layout)

        main_layout.addWidget(self.stack)

        # Tab button setup
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

        # Set background color for the main view
        widget = QWidget()
        widget.setLayout(main_layout)
        widget.setAutoFillBackground(True)
        palette = widget.palette()
        palette.setColor(QPalette.Window, QColor(245, 245, 245))
        widget.setPalette(palette)

        self.setCentralWidget(widget)

    # Tab buttoms to pressent the diffrent views
    def btn_company(self):
        self.stack.setCurrentIndex(0)

    def btn_association(self):
        self.stack.setCurrentIndex(1)

    def btn_inProgress(self):
        self.stack.setCurrentIndex(2)

    def btn_employees(self):
        self.stack.setCurrentIndex(3)

    def tab_label(self, title):
        """Create and design the label that is at the top of each view
        """
        label = QLabel(title)
        label.setMaximumHeight(50)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet(
            'color: rgb(54, 54, 54); font-family: Arial, Helvetica, sans-serif; font-weight: bold; font-size: 30px;')
        return label

    def stack_oneUI(self):
        """View for the company tab
        """
        container = QVBoxLayout()
        header_labels = ["Name", "Category", "Contact",
                         "Phone number", "Mail", "Joined", "Employee", "id"]
        data = self.db_controller.fill_company_table()
        table = self.setup_table(data, header_labels)
        container.addWidget(self.tab_label(self.titles[0]))
        container.addWidget(table)
        self.stack_one.setLayout(container)

    def stack_twoUI(self):
        """View for the association tab
        """
        container = QVBoxLayout()
        header_labels = ["Name", "Category", "Contact",
                         "Phone number", "Mail", "Joined", "Employee", "id"]
        data = self.db_controller.fill_association_table()
        data = [data]
        table = self.setup_table(data, header_labels)
        container.addWidget(self.tab_label(self.titles[1]))
        container.addWidget(table)
        self.stack_two.setLayout(container)

    def stack_threeUI(self):
        """View for the state tab
        """
        container = QVBoxLayout()
        header_labels = ["Name", "Category", "Contact",
                         "Phone number", "Mail", "Joined", "Employee", "id"]
        data = self.db_controller.fill_company_table()
        table = self.setup_table(data, header_labels)
        container.addWidget(self.tab_label(self.titles[2]))
        container.addWidget(table)
        self.stack_three.setLayout(container)

    def stack_fourUI(self):
        """View for the employee tab
        """
        container = QVBoxLayout()
        container.addWidget(self.tab_label(self.titles[3]))
        container.addWidget(EmployeeGrid(self.db_controller).employee_grid())
        self.stack_four.setLayout(container)

    def setup_table(self, data, header_labels):
        """Fill the TableView in att the company tab with data needed from the company table
        """
        table = QTableView()
        self.model = TableModel(data, header_labels)
        table.setModel(self.model)
        table.setShowGrid(False)
        table.clicked.connect(self.open_company_form)
        table.setStyleSheet(
            "QTableView::item {border-bottom: 1px solid #d6d9dc;} QTableView {background: #2b2f3b; color: #f5f5f5; }")

        return table
    
    def open_company_form(self, i):
        """Open the QWidget holding the information about the specific company_form
        Close when QWidget is closed by the user.
        """
        id = self.model.index(i.row(), 7).data()
        self.w = CompanyForm(id, self.db_controller)
        self.w.show()