from model import MysqlDB

'''
Script containing all queries the application using to select or commit to the mysql database
The class DatabaseController is dependent on the class MysqlDB
'''

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
        query = ("select employee.id, name, manager, sum(amount) from employee, "
                "employee_sales where employee.id = employee_id group by employee_id, name order by id")
        emp = self.db.execute_select_query(query)
        return emp

    def employees_company_count(self, id):
        query = f"select count(employee_id) from company where employee_id = {id}"
        count = self.db.execute_select_query(query)
        return count[0][0]
    
    def top_five(self):
        query = "select name, amount, year from top_sales join employee on employee.id = employee_id order by amount desc limit 5"
        top_5 = self.db.execute_select_query(query)
        return top_5

    def company_tabel(self, id):
        query = f"select * from company where id = {id}"
        comp_tabel = self.db.execute_select_query(query)
        return comp_tabel

    def company_name(self, id):
        query = f"select name from company where id = {id}"
        name = self.db.execute_select_query(query)
        return name

    def company_offers(self, id):
        query = f"select id, offer from offer where company_id = {id}"
        company_offers = self.db.execute_select_query(query)
        return company_offers

    def company_city(self, id):
        query = f"select city from offer where company_id = {id}"
        city = self.db.execute_select_query(query)
        return city

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
    
    def add_offer(self, company_id, offer, city):
        query = f"insert into offer (company_id, offer, city) values ({company_id}, '{offer}', '{city}')"
        self.db.execute_query(query)
    
    def update_app_info(self, phone, address, mail, web, terms, open, desc, id):
        query = (f"update offer_info set phone_number = '{phone}', address = '{address}', mail = '{mail}', web = '{web}', "
                f"terms = '{terms}', opening_hours = '{open}', description = '{desc}' where id = {id}")
        self.db.execute_query(query)
    
    def update_company_table(self, name, phone, contact, address, mail, date, notes, sells, asso, joined, id):
        query = (f"Update company set name = '{name}', phone_number = '{phone}', contact = '{contact}', address = '{address}', "
                f"mail = '{mail}', joined_date = {date}, notes = '{notes}', sells = '{sells}', association = '{asso}', joined = '{joined}' where id = {id}")
        self.db.execute_query(query)
        
    def update_offer(self, offer, id):
        query = f"Update offer set offer = '{offer}' where id = {id}"
        self.db.execute_query(query)
    
    def delete_offer(self, id):
        query =f"delete from offer where id = '{id}'"
        self.db.execute_query(query)
    
    def delete_app_info(self, id):
        query = f"delete from offer_info where id = '{id}'"
        self.db.execute_query(query)

    def disconnect(self):
        self.db.disconnect()
