class person:
    name="Adip"

    def study(self):
        print("I study in Harvard University.")

class employee(person):
    company="Neuralink"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def study(self):
        print(f"I take online classes.")

class programmmer(employee):
    company="Google"

    def getSalary(self):
        print(f"Salary is $1000000.")

    def study(self):
        print(f"I have completed my study.")

a=person()
b=employee()
c=programmmer()

# print(a.company)

print(c.name)
c.getSalary()

a.study()
b.study()
c.study()