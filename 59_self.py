class Employee:
    company='Facebook'
    salary='$1,00,000'
    def giveSalary(self):
        print(f"Salary of {self.name}, working in {self.company}, is {self.salary}.")

# Here, we have created a class Employee with class attributes company and salary.
# We have created two objects Adip and Arjun of the class Employee.
# self is a reference to the current instance of the class.
# We have created a method giveSalary() which takes self as an argument.
# We have used self to access the class attributes inside the method.
# We have called the method using the object Adip and Arjun.
    
Adip=Employee()
Adip.name='Adip'
Adip.company='Google'
Adip.salary='$1,50,000'
Adip.giveSalary()           # >>Employee.giveSalary(Adip)

Arjun=Employee()
Arjun.name='Arjun'
Arjun.giveSalary()           # >>Employee.giveSalary(Arjun)