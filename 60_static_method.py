class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print(f"The time is 9AM in the morning")

Adip = Employee()
Adip.salary = 100000
Adip.getSalary("Thanks!")      # Thanks!  >is the signature for Adip
Adip.greet() # Employee.greet()
Adip.time()

