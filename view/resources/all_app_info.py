from PyQt5 import QtCore
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget


class AllAppInfo(QWidget):
    """QWidget presenting a user with the offer_info content, the user can delete, change and add to the database
    """

    def __init__(self, db_controller, company_id, row):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle("Information in app")
        self.company_id = company_id
        self.db_controller = db_controller
        self.data = self.db_controller.all_app_info(self.company_id)
        self.id = int(self.data[row][0])
        self.data = self.data[row][1:]
        self.setup_dict()
        self.gui_setup()

    def gui_setup(self):
        """Setup the QWidget layout
        """
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        left_side = QFormLayout()
        right_side = QFormLayout()

        '''
        Left side of the layout
        '''
        phone = QLineEdit()
        phone.setText(self.dict["Phone"])
        phone.setObjectName("Phone")
        phone.textChanged.connect(self.edit_change)
        left_side.addRow(QLabel("Phone number"), phone)

        address = QLineEdit()
        address.setMinimumWidth(210)
        address.setText(self.dict["Address"])
        address.setObjectName("Address")
        address.textChanged.connect(self.edit_change)
        left_side.addRow(QLabel("Address"), address)

        mail = QLineEdit()
        mail.setText(self.dict["Mail"])
        mail.setMinimumWidth(210)
        mail.setObjectName("Mail")
        mail.textChanged.connect(self.edit_change)
        left_side.addRow(QLabel("Mail"), mail)

        web = QLineEdit()
        web.setText(self.dict["Web"])
        web.setMinimumWidth(210)
        web.setObjectName("Web")
        web.textChanged.connect(self.edit_change)
        left_side.addRow(QLabel("Web"), web)

        self.terms = QTextEdit()
        self.terms.setText(self.dict["Terms"])
        self.terms.textChanged.connect(self.terms_change)
        left_side.addRow(QLabel("Terms"), self.terms)

        '''
        Right side of the layout
        '''
        self.open_hours = QTextEdit()
        self.open_hours.setText(self.dict["Open"])
        self.open_hours.textChanged.connect(self.open_change)
        right_side.addRow(QLabel("Opening hours"), self.open_hours)

        self.description = QTextEdit()
        self.description.setText(self.dict["Desc"])
        self.description.textChanged.connect(self.description_change)
        right_side.addRow(QLabel("description"), self.description)

        # Buttom buttons
        delete_btn = QPushButton("Delete")
        delete_btn.pressed.connect(self.delete)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.pressed.connect(self.cancel)
        submit_btn = QPushButton("Submit")
        submit_btn.pressed.connect(self.submit)

        end = QHBoxLayout()
        end.addWidget(delete_btn)
        end.addWidget(QLabel(" "))
        end.addWidget(cancel_btn)
        end.addWidget(submit_btn)

        form_layout.addLayout(left_side)
        form_layout.addLayout(right_side)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(end)

        self.setLayout(main_layout)

    def setup_dict(self):
        """Get data from the database into the dictionary
        """
        self.dict = {
            "Phone": self.data[0],
            "Address": self.data[1],
            "Mail": self.data[2],
            "Web": self.data[3],
            "Terms": self.data[4],
            "Open": self.data[5],
            "Desc": self.data[6]
        }

    def edit_change(self, text):
        """If a QLineEdit() Widget inputfield is changed the input will be set in the dictionary
        """
        sender = self.sender().objectName()
        self.dict[sender] = text

    # Insert QTextEdit changes to the dictionary (Next three methods)
    def terms_change(self):
        text = self.terms.toPlainText()
        self.dict["Terms"] = text

    def open_change(self):
        text = self.open_hours.toPlainText()
        self.dict["Open"] = text

    def description_change(self):
        text = self.description.toPlainText()
        self.dict["Desc"] = text

    def delete(self):
        """Display a QMessageBox asking the a user if they really want to delete app_info content
        """
        check = QMessageBox.question(self, "Remove", f"Remove info?")
        if check == QMessageBox.Yes:
            self.db_controller.delete_app_info(self.id)
            self.close()

    def cancel(self):
        """Close this QWidget
        """
        self.close()

    def submit(self):
        """Submit all changes to the database
        """
        self.db_controller.update_app_info(self.dict["Phone"], self.dict["Address"], self.dict["Mail"],
                                           self.dict["Web"], self.dict["Terms"], self.dict["Open"], self.dict["Desc"], self.id)
        self.close()
