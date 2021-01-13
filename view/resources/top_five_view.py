from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

class TopFive(QWidget):
    def __init__(self, db_controller):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setGeometry(400, 300, 500, 400)
        self.setWindowTitle("Top Five sales records over the years")
        self.data = db_controller.top_five()
        self.gui_setup()
    
    def gui_setup(self):
        self.main_layout = QVBoxLayout()
        self.label_list()
        self.setLayout(self.main_layout)
        
        
    def label_list(self):
        for i in range(len(self.data)):
            record = QLabel(f"{i+1}. {self.data[i][0]}  {self.data[i][1]} app-code's, year {self.data[i][2]}")
            record.setStyleSheet("color: #f5f5f5; font-family: Arial, Helvetica, sans-serif; "
                        "font-weight: bold; font-size: 30px; background-color: #2b2f3b; margin: 10px;")
            self.main_layout.addWidget(record)