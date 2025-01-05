class Employee:
    company='Facebook'                  # here company is a class attribute
    salary = '$15000'

Adip=Employee()
Arjun=Employee()

Adip.salary='$2500000'
Arjun.salary='$3000000'

print(Adip.company)                     # returns default value of company as we have not changed it
print(Adip.salary)
print(Arjun.salary)

Employee.company='YouTube'
print(Arjun.company)

# Here, we have created a class Employee with class attributes company and salary.
# We have created two objects Adip and Arjun of the class Employee.
# We have changed the salary of Adip and Arjun objects.
# We have changed the class attribute company to YouTube.