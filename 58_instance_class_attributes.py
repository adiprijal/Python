class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
harry.salary = 300
print(harry.salary)             # Output: 300
print(rajni.salary)             # Output: 100

# Below line throws an error as address is not present in instance/class 
print(rajni.address) 