from view.resources.offers_handler_view import OffersHandler
from view.resources.app_info_view import AppInfo
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QCheckBox, QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout, QInputDialog, QLabel, QLineEdit, QListView, QListWidget, QListWidgetItem, QMessageBox, QPushButton, QRadioButton, QTextEdit, QVBoxLayout, QWidget
from view.gui import QMainWindow

'''
Help class to make the QLabel date clickable
'''
class DateLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == QtCore.Qt.LeftButton:
            self.clicked.emit()


class CompanyForm(QWidget):
    def __init__(self, company_id, db_controller):
        super().__init__()
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setGeometry(500, 300, 800, 300)
        
        self.company_id = company_id
        self.db_controller = db_controller
        self.data = self.db_controller.company_tabel(company_id)
        self.city = self.db_controller.company_city(company_id)
        self.city = self.city[0][0] if self.city is not None else None 
        self.setup_dict()
        self.db_controller = db_controller
        
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
        company_edit.setText(self.dict["name"])
        company_edit.setObjectName("name")
        company_edit.textChanged.connect(self.edit_change)
        left_form.addRow(company_name, company_edit)

        # Date joined
        date_label = QLabel("Joined: ")
        self.date = DateLabel()
        date_joined = self.dict["joined_date"].strftime('%-Y/%-m/%-d') if self.dict["joined_date"] is not None else "Click to set date"
        self.date.setText(date_joined)
        self.date.clicked.connect(self.change_date)
        left_form.addRow(date_label, self.date)

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
        self.ass_check = QCheckBox("Association")
        is_ass = True if self.dict["asso"] == 1 else False
        print("Asso", is_ass)
        self.ass_check.setChecked(is_ass)
        left_form.addWidget(self.ass_check)

        # Radio btn company joined
        joined_btn = QHBoxLayout()
        self.joined_yes = QRadioButton("Yes")
        joined_no = QRadioButton("No")
        self.joined_yes.setChecked(self.dict["joined"] == 1)
        joined_no.setChecked(self.dict["joined"] == 0)
        joined_btn.addWidget(self.joined_yes)
        joined_btn.addWidget(joined_no)
        left_form.addRow(QLabel("Joined"), joined_btn)
        left_side.addLayout(left_form)

        # ListView for the offers
        offers_label = QLabel("Offers:")
        left_side.addWidget(offers_label)
        self.offer_list = QListWidget()
        self.offer_list.itemClicked.connect(self.list_clicked)
        self.offer_list.setMaximumHeight(70)
        self.add_to_QList()
        left_side.addWidget(self.offer_list)

        # Add offer btn and show app info btn
        offers_appInfo_btns = QHBoxLayout()
        self.offers = QPushButton("Add offer")
        self.offers.setMaximumWidth(100)
        self.offers.pressed.connect(self.clicked_offers)
        self.app_info = QPushButton("App information")
        self.app_info.setMaximumWidth(120)
        self.app_info.pressed.connect(self.clicked_app_info)
        offers_appInfo_btns.addWidget(self.offers)
        offers_appInfo_btns.addWidget(self.app_info)
        left_side.addLayout(offers_appInfo_btns)
        
        main_layout.addLayout(left_side)

        '''
        Left-side form end
        '''

        '''
        Right-side form start
        '''
        # Contact name
        contact_edit = QLineEdit()
        contact_edit.setText(self.dict["contact"])
        contact_edit.setObjectName("contact")
        contact_edit.textChanged.connect(self.edit_change)
        right_form.addRow(QLabel("Contact"), contact_edit)

        # Phone number
        phone_edit = QLineEdit()
        phone_edit.setText(self.dict["phone"])
        phone_edit.setObjectName("phone")
        phone_edit.textChanged.connect(self.edit_change)
        right_form.addRow(QLabel("Phone number"), phone_edit)

        # Address
        address = QLineEdit()
        address.setMinimumWidth(240)
        address.setText(self.dict["address"])
        address.setObjectName("address")
        address.textChanged.connect(self.edit_change)
        right_form.addRow(QLabel("Address"), address)

        # City
        city = QLineEdit()
        city.setText(self.city)
        city.textChanged.connect(self.city_change)
        right_form.addRow(QLabel("City"), city)

        # Mail
        mail_edit = QLineEdit()
        mail_edit.setMinimumWidth(240)
        mail_edit.setText(self.dict["mail"])
        mail_edit.setObjectName("mail")
        mail_edit.textChanged.connect(self.edit_change)
        right_form.addRow(QLabel("E-mail"), mail_edit)

        # Notes
        notes_edit = QTextEdit()
        notes_edit.setText(self.dict["notes"])
        right_form.addRow(QLabel("Notes"), notes_edit)
        
        

        end_button = QHBoxLayout()
        cancel = QPushButton("Cancel")
        cancel.setMinimumWidth(130)
        cancel.clicked.connect(self.quit)
        submit = QPushButton("Submit")
        submit.setMinimumWidth(130)
        submit.clicked.connect(self.submit)
        end_button.addWidget(cancel)
        end_button.addWidget(submit)
        right_form.addRow(QLabel(""), end_button)
        right_side.addLayout(right_form)
        main_layout.addLayout(right_side)
        
        
        

        '''
        Right-side form end
        '''

        self.setLayout(main_layout)
       
    
    def add_to_QList(self):
        offers = self.db_controller.company_offers(self.company_id)
        self.id_list = []
        if offers is not None:
            for i in range(len(offers)):
                self.id_list.append(offers[i][0])
                self.offer_list.addItem(offers[i][1])

    def list_clicked(self, offer):  
        self.w = OffersHandler(offer, self.city, self.id_list[self.offer_list.currentRow()], self.db_controller)
        self.w.show() 

    def clicked_sales(self):
        print("Clicked on sales stats")

    def clicked_offers(self):
        offer, ok = QInputDialog.getText(self,"Add offer", "Enter offer")
        if ok:
            self.offer_list.addItem(offer)
            self.db_controller.add_offer(self.company_id, offer, self.city)
    
    def clicked_app_info(self):
        self.w = AppInfo(self.db_controller, self.company_id)
        self.w.show()
    
    def change_date(self):
        date, ok = QInputDialog.getText(self,"Set date company joined", "Enter date (YYYY-MM-DD)")
        if ok:
            self.dict["joined_date"] = date
            self.date.setText(date)
    
    def edit_change(self, text):
        sender = self.sender().objectName()
        self.dict[sender] = text
    
    def city_change(self, text):
        self.city = text
    
    def set_sales_status(self):
        if self.dict["sells"] == 1:
            self.sale_yes.setChecked(True)
        else:
            self.sale_no.setChecked(True) 
            self.sales_stats.hide()

    def show_sales_state_btn(self):
        self.sales_stats.show()

    def hide_sales_state_btn(self):
        self.sales_stats.hide()
    
    def setup_dict(self):
        self.dict = {
            "name": self.data[0][2],
            "phone": self.data[0][3],
            "contact": self.data[0][4],
            "address": self.data[0][5],
            "mail": self.data[0][6],
            "joined_date": self.data[0][8],
            "notes": self.data[0][9],
            "sells": self.data[0][10],
            "asso": self.data[0][11],
            "joined": self.data[0][12]
        }

    def submit(self):
        sells = 1 if self.sale_yes.isChecked() == True else 0
        joined = 1 if self.joined_yes.isChecked() == True else 0
        asso = 1 if self.ass_check.isChecked() == True else 0
        joined_date = f"\'{self.dict['joined_date']}\'" if self.dict["joined_date"] is not None else "null"
        print(joined_date)
        self.db_controller.update_company_table(self.dict["name"], self.dict["phone"], self.dict["contact"],
             self.dict["address"], self.dict["mail"], joined_date, self.dict["notes"], 
             sells, asso, joined, self.company_id)
        self.close()
       

    def quit(self):
        self.close()