from controller import DatabaseController
from view import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
window.db_controller.disconnect()