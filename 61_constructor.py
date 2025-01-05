class Employee:
    company = "Google"


    # Constructor is a special type of method which is used to initialize the instance members of the class.
    # Constructor is called when an object is created.
    # Constructor has a special name __init__.
    # Constructor can take parameters.
    def __init__(self, name , salary , Address ,subunit):
        self.name=name
        self.salary=salary
        self.Address=Address
        self.subunit=subunit
        print("New Employee Recruited...")

    def getData(self):
        print(f"The name of new employee is {self.name}.")
        print(f"The salary of {self.name} is {self.salary}.")
        print(f"{self.name} is from {self.Address}.")
        print(f"{self.name} is recruited in sub-unit {self.subunit}.")


Adip=Employee("Adip","$500000",'Nepal',"YouTube")                   # Code inside the constructor is executed when the object is created.
# Employee.__init__(Adip,"Adip","$500000",'Nepal',"YouTube")
Adip.getData()