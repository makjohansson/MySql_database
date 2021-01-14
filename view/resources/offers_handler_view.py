from PyQt5 import QtCore
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget

class OffersHandler(QWidget):
    """QWidget to change or remove a offer related to a specific company
    """
    def __init__(self, offer, city, offer_id, db_controller):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setGeometry(600, 330, 500, 150)
        self.setWindowTitle("Change/Remove")

        self.db_controller = db_controller
        self.offer = offer
        self.city = city
        self.offer_id = offer_id
        self.setup_gui()

        

    def setup_gui(self):
        """QWidget layout created 
        """
        main_layout = QVBoxLayout()
        edit_layout = QFormLayout()
        btn_layout = QHBoxLayout()

        self.edit_offer = QLineEdit()
        self.edit_offer.setMinimumWidth(400)
        self.edit_offer.setText(self.offer.text())
        edit_layout.addRow(QLabel("Offer"), self.edit_offer)
        main_layout.addLayout(edit_layout)

        submit_btn = QPushButton("Submit")
        submit_btn.clicked.connect(self.submit)
        delete_btn = QPushButton("Delete")
        delete_btn.clicked.connect(self.delete)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.cancel)
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(delete_btn)
        btn_layout.addWidget(submit_btn)
        main_layout.addLayout(btn_layout)

        
        self.setLayout(main_layout)
    
    def submit(self):
        """Update database with changes made
        """
        self.offer.setText(self.edit_offer.text())
        self.db_controller.update_offer(self.edit_offer.text(), self.offer_id)
        self.close()
    
    def delete(self):
        """Remove offer form the offer table
        """
        check = QMessageBox.question(self, "Remove", f"Remove this offer?\n\n{self.offer.text()}")
        if check == QMessageBox.Yes:
            self.offer.setHidden(True)
            self.db_controller.delete_offer(self.offer_id)
            self.close()
        
    def cancel(self):
        """Close this QWidget
        """
        self.close()
