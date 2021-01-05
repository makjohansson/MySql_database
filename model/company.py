
class Company():

    def __init__(self, id, name, phone_number, contact, address, mail, category, join_date, notes, sells, association, joined):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.contact = contact
        self.address = address
        self.mail = mail
        self.category = category
        self.join_date = join_date
        self.notes = notes
        self.sells = sells
        self.association = association
        self.joined = joined
        self.employee = ""

    def set_employee(self, employee):
        self.employee = employee
    
    