class Employer:
    salary = 30000

    def __init__(self, age, name, tax):
        self.age = age
        self.name = name
        self.tax = tax

    def salary_calculation(self, tax):
        tax_rate = 100 - tax
        self.salary = self.salary * tax_rate / 100


    def scheck_salary(self):
        self.salary_calculation(self.tax)
        return self.salary

if __name__ == '__main__':
    employe = Employer('SomeName', 25, 10)
    print(employe.name)
    print(employe.tax)
    print(employe.age)
    print(employe.scheck_salary())