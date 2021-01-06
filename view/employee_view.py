
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QWidget


class EmployeeGrid():
    def __init__(self, db_controller):
        self.db_controller = db_controller

    def employee_grid(self):
        grid = QVBoxLayout()
        row_one = QHBoxLayout()
        row_two = QHBoxLayout()
        
        QLabels = self.__fill_grid()
        pixmap = QPixmap('view/img/avatar.png')
        pixmap_girl = QPixmap('view/img/avatar_girl.png')

        label = QLabel()
        label.setPixmap(pixmap)
        label.setMaximumSize(pixmap.width(), pixmap.height())
        row_one.addWidget(label)
        row_one.addWidget(QLabels[0])

        label = QLabel()
        label.setPixmap(pixmap_girl)
        label.setMaximumSize(pixmap_girl.width(), pixmap_girl.height())
        row_one.addWidget(label)
        row_one.addWidget(QLabels[1])
        
        label = QLabel()
        label.setPixmap(pixmap_girl)
        label.setMaximumSize(pixmap_girl.width(), pixmap_girl.height())
        row_two.addWidget(label)
        row_two.addWidget(QLabels[2])

        label = QLabel()
        label.setPixmap(pixmap_girl)
        label.setMaximumSize(pixmap_girl.width(), pixmap_girl.height())
        row_two.addWidget(label)
        row_two.addWidget(QLabels[3])
        
        grid.addLayout(row_one)
        grid.addLayout(row_two)
        widget = QWidget()
        widget.setLayout(grid)
        return widget
    
    def __fill_grid(self):
        QLabels = []
        emp_info = ""
        data = self.db_controller.employee_info()
    
        for row in range(len(data)):
            count = self.db_controller.employees_company_count(data[row][0])
            role = "Manager" if data[row][2] == None else "Sales" 
            emp_info = f"Name: {data[row][1]}\nRole: {role}\nApp-code's sold: {data[row][3]}\nCompanies: {count}"
            label = QLabel(emp_info)
            label.setStyleSheet("""
                color: rgb(54, 54, 54);
                font-family: Arial, Helvetica, sans-serif;
                font-size: 15px;
            """)
            QLabels.append(label)
        return QLabels