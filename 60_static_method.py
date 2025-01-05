class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    # self.company takes the value of Adip.company


    # Static Method is a method which is bound to the class and not the object of the class.
    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print(f"The time is 9AM in the morning.")

Adip = Employee()
# Adip.company = "Microsoft"
Adip.salary = 100000

# we don't need to pass self while calling the method
# Adip.getSalary(Adip, "Thanks!")  == Adip.getSalary("Thanks!")
Adip.getSalary("Thanks!")

Adip.greet() 
Employee.greet()
Adip.time()
Employee.time()
# We don't need to pass object name[self] while calling a static method.   eg : line 27, 29
# We can call a static method using the object name or the class name.