from model import MysqlDB


class DatabaseController():
    def __init__(self):
        self.db = MysqlDB()

    def fill_company_table(self):
        query = ("select company.name, category, contact, phone_number, mail, joined, employee.name, "
                 "company.id from company left join employee on employee.id = company.employee_id where association = 0 ")
        companies = self.db.execute_select_query(query)
        return companies

    def fill_association_table(self):
        query = ("select company.name, category, contact, phone_number, mail, joined, employee.name, "
                 "company.id from company left join employee on employee.id = company.employee_id where association = 1 ")
        associations = self.db.execute_select_query(query)
        return associations

    def employee_info(self):
        query = ("select employee.id, name, manager, amount, year from employee "
                 "join employee_sales ON employee_id = employee.Id")
        emp = self.db.execute_select_query(query)
        return emp

    def employees_company_count(self, id):
        query = f"select count(employee_id) from company where employee_id = {id}"
        count = self.db.execute_select_query(query)
        return count[0][0]

    def company_tabel(self, id):
        query = f"select * from company where id = {id}"
        comp_tabel = self.db.execute_select_query(query)
        return comp_tabel

    def company_name(self, id):
        query = f"select name from company where id = {id}"
        name = self.db.execute_select_query(query)
        return name

    def company_offers(self, id):
        query = f"select offer from offer where company_id = {id}"
        company_offers = self.db.execute_select_query(query)
        return company_offers

    def app_info(self, id):
        query = (f"select phone_number, address, mail from offer_info where " 
                f"offer_id in (select id from offer where company_id = {id})")
        app_info = self.db.execute_select_query(query)
        return app_info

    def all_app_info(self, id):
        query = (f"select id, phone_number, address, mail, web, terms, opening_hours, description " 
                f"from offer_info where offer_id in (select id from offer where company_id = {id})")
        all_app_info =self.db.execute_select_query(query)
        return all_app_info
    
    def update_app_info(self, phone, address, mail, web, terms, open, desc, id):
        query = (f"update offer_info set phone_number = '{phone}', address = '{address}', mail = '{mail}', web = '{web}', "
                f"terms = '{terms}', opening_hours = '{open}', description = '{desc}' where id = {id}")
        self.db.execute_update_query(query)
        

    def disconnect(self):
        self.db.disconnect()
