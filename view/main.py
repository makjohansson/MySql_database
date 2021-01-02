from PyQt5.QtWidgets import QMainWindow, QPushButton, QStackedLayout
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QApplication
from PyQt5.QtCore import Qt
import sys

from PyQt5 import QtCore

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

        titles = ['Company', 'Association', 'inProgress', 'Employess']
        main_layout = QHBoxLayout()
        btn_layout = QVBoxLayout()
        self.stacked_layout = QStackedLayout()

        main_layout.addLayout(btn_layout)
        main_layout.addLayout(self.stacked_layout)

        
        company_btn = QPushButton(titles[0])
        company_btn.pressed.connect(self.btn_company)
        btn_layout.addWidget(company_btn)
        
        ass_btn = QPushButton(titles[1])
        ass_btn.pressed.connect(self.btn_association)
        btn_layout.addWidget(ass_btn)

        inProg_btn = QPushButton(titles[2])
        inProg_btn.pressed.connect(self.btn_inProgress)
        btn_layout.addWidget(inProg_btn)

        emp_btn = QPushButton(titles[3])
        emp_btn.pressed.connect(self.btn_employees)
        btn_layout.addWidget(emp_btn)

        btn_layout.setAlignment(QtCore.Qt.AlignTop)

        self.stacked_layout.addWidget(TestLabel(titles[0]))
        self.stacked_layout.addWidget(TestLabel(titles[1]))
        self.stacked_layout.addWidget(TestLabel(titles[2]))
        self.stacked_layout.addWidget(TestLabel(titles[3]))

        self.stacked_layout.setCurrentIndex(0)

        
        
        widget = QWidget()
        widget.setLayout(main_layout)
        
        self.setCentralWidget(widget)
    
    def btn_company(self):
        self.stacked_layout.setCurrentIndex(0)
    
    def btn_association(self):
        self.stacked_layout.setCurrentIndex(1)

    def btn_inProgress(self):
        self.stacked_layout.setCurrentIndex(2)
    
    def btn_employees(self):
        self.stacked_layout.setCurrentIndex(3)




app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()