class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
harry.salary = 300
harry.salary = 30
# rajni.salary = 400
print(harry.salary)
print(rajni.salary)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 