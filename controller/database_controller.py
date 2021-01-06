from model import MysqlDB


class DatabaseController():
    def __init__(self):
        self.db = MysqlDB()

    def fill_company_table(self):
        query = ("select company.name, category, contact, phone_number, mail, joined, employee.name, "
                 "company.id from company left join employee on employee.id = company.employee_id where association = 0 ")
        companies = self.db.execute_query(query)
        return companies
    
    def fill_association_table(self):
        query = ("select company.name, category, contact, phone_number, mail, joined, employee.name, "
                 "company.id from company left join employee on employee.id = company.employee_id where association = 1 ")
        associations = self.db.execute_query(query)
        return associations

    def employee_info(self):
        query = ("select employee.id, name, manager, amount, year from employee "
                 "join employee_sales ON employee_id = employee.Id")
        emp = self.db.execute_query(query)
        return emp
    
    def employees_company_count(self, id):
        query = f"select count(employee_id) from company where employee_id = {id}"
        count = self.db.execute_query(query)
        return count[0][0]
    
    def company_tabel(self, id):
        query = f"select * from company where id = {id}"
        comp_tabel = self.db.execute_query(query)
        return comp_tabel

    def disconnect(self):
        self.db.disconnect()
