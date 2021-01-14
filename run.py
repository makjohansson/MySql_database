from view import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

"""
Script used to run the application
"""

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
window.db_controller.disconnect()