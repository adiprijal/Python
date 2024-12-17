class Employee:
    company='Facebook'
    salary = '$15000'

Adip=Employee()
Arjun=Employee()

Adip.salary='$2500000'
Arjun.salary='$3000000'

print(Adip.company)
print(Adip.salary)
print(Arjun.salary)

Employee.company='YouTube'
print(Arjun.company)