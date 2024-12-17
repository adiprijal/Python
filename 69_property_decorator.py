class Employee:
    company = "Coca Cola"
    salary = 200000
    salarybonus = 5000
    # totalSalary =205000

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary

e = Employee()
# print(e.totalSalary)
e.totalSalary =256789
print(e.salary)
print(e.salarybonus)