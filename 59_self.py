class Employee:
    company='Facebook'
    salary='$1,00,000'
    def giveSalary(self):
        print(f"Salary of {self.name}, working in {self.company}, is {self.salary}.")
    
Adip=Employee()
Adip.name='Adip'
Adip.company='Google'
Adip.salary='$1,50,000'
Adip.giveSalary()           # >>Employee.giveSalary(Adip)

Arjun=Employee()
Arjun.name='Arjun'
Arjun.giveSalary()           # >>Employee.giveSalary(Arjun)