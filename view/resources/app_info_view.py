
from view.resources.all_app_info import AllAppInfo
from PyQt5 import QtCore
from view.resources.tablemodel import TableModel
from PyQt5.QtWidgets import QTableView, QVBoxLayout, QWidget, QLabel


class AppInfo(QWidget):
    """QWidget contaning a QTableView presenting a user with the offer_info related with the copany
    """
    def __init__(self, db_controller, company_id):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setGeometry(520, 320, 760, 200)
        self.company_id = company_id
        self.db_controller = db_controller
        self.data = self.db_controller.app_info(self.company_id)
        title = self.db_controller.company_name(self.company_id)
        self.setWindowTitle(title[0][0])
        self.header_labels = ["Phone number", "Address", "Mail"]
        self.gui_setup()
    
    def gui_setup(self):
        main_layout = QVBoxLayout()
        title = QLabel("App information")
        table = QTableView()
        model = TableModel(self.data, self.header_labels, main_tabel=False)
        table.setModel(model)

        table.setShowGrid(False)
        table.resizeColumnsToContents()
        table.clicked.connect(self.app_info)
        table.setStyleSheet(
            "QTableView::item {border-bottom: 1px solid #d6d9dc; } QTableView {background: #2b2f3b; color: #f5f5f5;}")

        main_layout.addWidget(title)
        main_layout.addWidget(table)

        self.setLayout(main_layout)

    def app_info(self, i):
        """Open the row in the TableView, showing the information that offer_info contaning
        """
        row = i.row()
        self.w = AllAppInfo(self.db_controller, self.company_id, row)
        self.w.show()