from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QCheckBox, QFormLayout, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QTextEdit, QVBoxLayout, QWidget
from view.gui import QMainWindow


class DateLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()


class CompanyForm(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setGeometry(500, 300, 800, 300)
        window_title = self.data[0][2]
        self.setWindowTitle(window_title)

        # self.setStyleSheet("QLabel{background-color: yel;}")

        main_main = QVBoxLayout()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        left_side = QVBoxLayout()
        left_form = QFormLayout()

        right_side = QVBoxLayout()
        right_form = QFormLayout()

        '''
        Left-side form start
        '''

        # Company name
        company_name = QLabel("Company")
        company_edit = QLineEdit()
        company_edit.setMinimumWidth(270)
        company_edit.setText(data[0][2])
        company_edit.textChanged.connect(self.company_text)
        left_form.addRow(company_name, company_edit)

        # Date joined
        date_label = QLabel("Joined: ")
        date = DateLabel()
        date_joined = data[0][8] if data[0][8] is not None else "Click to set date"
        date.setText(date_joined)
        date.clicked.connect(self.change_date)
        left_form.addRow(date_label, date)

        # Sells app-codes
        sells_btn = QHBoxLayout()
        self.sale_yes = QRadioButton("Yes")
        self.sale_yes.clicked.connect(self.show_sales_state_btn)
        self.sale_no = QRadioButton("No")
        self.sale_no.clicked.connect(self.hide_sales_state_btn)

        sells_btn.addWidget(self.sale_yes)
        sells_btn.addWidget(self.sale_no)
        left_form.addRow(QLabel("Sell's app-codes"), sells_btn)

        # Sales stats btn
        self.sales_stats = QPushButton("Sales stats")
        self.sales_stats.pressed.connect(self.clicked_sales)
        self.set_sales_status()
        left_form.addWidget(self.sales_stats)

        # Association radio checkBox
        ass_check = QCheckBox("Association")
        is_ass = True if data[0][11] == 1 else False
        ass_check.setChecked(is_ass)
        left_form.addWidget(ass_check)

        # Radio btn company joined
        joined_btn = QHBoxLayout()
        joined_yes = QRadioButton("Yes")
        joined_no = QRadioButton("No")
        joined_yes.setChecked(True)
        joined_btn.addWidget(joined_yes)
        joined_btn.addWidget(joined_no)
        left_form.addRow(QLabel("Joined"), joined_btn)

        # Offers btn
        self.offers = QPushButton("Offers")
        self.offers.pressed.connect(self.clicked_offers)
        left_form.addWidget(self.offers)
        left_side.addLayout(left_form)
        main_layout.addLayout(left_side)

        '''
        Left-side form end
        '''

        '''
        Right-side form start
        '''
        # Contact name
        contact_edit = QLineEdit()
        contact_edit.setText(self.data[0][4])
        contact_edit.textChanged.connect(self.contact_text)
        right_form.addRow(QLabel("Contact"), contact_edit)

        # Phone number
        phone_edit = QLineEdit()
        phone_edit.setText(self.data[0][3])
        right_form.addRow(QLabel("Phone number"), phone_edit)

        # Address
        vbox = QVBoxLayout()
        add_one = QLineEdit()
        add_one.setMinimumWidth(240)
        add_one.setText(self.data[0][5])
        vbox.addWidget(add_one)
        right_form.addRow(QLabel("Address"), vbox)

        # Mail
        mail_edit = QLineEdit()
        mail_edit.setMinimumWidth(240)
        mail_edit.setText(self.data[0][6])
        right_form.addRow(QLabel("E-mail"), mail_edit)

        # Notes
        notes_edit = QTextEdit()
        notes_edit.setText(self.data[0][9])
        right_form.addRow(QLabel("Notes"), notes_edit)
        right_side.addLayout(right_form)
        

        end_button = QHBoxLayout()
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.quit)
        submit = QPushButton("Submit")
        end_button.addWidget(cancel)
        end_button.addWidget(submit)
        right_side.addLayout(end_button)
        main_layout.addLayout(right_side)
        
        
        

        '''
        Right-side form end
        '''

        #widget = QWidget()
        self.setLayout(main_layout)
        # self.setCentralWidget(widget)

    def clicked_sales(self):
        print("Clicked on sales stats")

    def clicked_offers(self):
        print("Clicked on offers")

    def change_date(self):
        print("clicked")

    def company_text(self, text):
        print(text)

    def contact_text(self, text):
        print(text)
    
    def set_sales_status(self):
        if self.data[0][10] == 1:
            self.sale_yes.setChecked(True)
        else:
            self.sale_no.setChecked(True) 
            self.sales_stats.hide()

    def show_sales_state_btn(self):
        self.sales_stats.show()

    def hide_sales_state_btn(self):
        self.sales_stats.hide()
    
    def quit(self):
        self.close()