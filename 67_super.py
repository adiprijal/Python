class person:
    name="Adip"

    def __init__(self) :
        print(f"The person is Adip.")        

    @staticmethod
    def study():
        print("I study in Harvard University.")

class employee(person):
    company="Neuralink"

    def __init__(self):
        super().__init__()
        print(f"The Employee is the person.")

    @staticmethod
    def getSalary():
        print(f"Salary is $50000.")

    @staticmethod
    def study():
        super().study()
        print(f"I take online classes.")

class programmer(employee):
    company="Google"

    def __init__(self):
        super().__init__()
        print("The programmer is the employee.")

    @staticmethod
    def getSalary():
        super().getSalary()
        print(f"Salary is $1000000.")

    @staticmethod
    def study():
        super().study()
        print(f"I have completed my study.")

# a=person()
# b=employee()
c=programmer()

# a.study()
# b.study()
# c.study()

# c.getSalary()
