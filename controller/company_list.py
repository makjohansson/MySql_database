from model import MysqlDB, Company

class CompanyList():
    def __init__(self):
        self.db = MysqlDB()
        self.companies = self.db.get_companies()
        

    def get_companies(self):
        companies = []
        for i in range(2):
            print(self.companies[i])

if __name__ == '__main__':
    C = CompanyList()
    C.get_companies()