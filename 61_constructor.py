class Employee:
    company = "Google"

    def __init__(self, name , salary , Address ,subunit):
        self.name=name
        self.salary=salary
        self.Address=Address
        self.subunit=subunit
        print("New Employee Recruited...")
        # print(f"")

    def getData(self):
        print(f"The name of new employee is {self.name}.")
        print(f"The salary of {self.name} is {self.salary}.")
        print(f"{self.name} is from {self.Address}.")
        print(f"{self.name} is recruited in subunit {self.subunit}.")


Adip=Employee("Adip","$500000",'Nepal',"YouTube")
Adip.getData()