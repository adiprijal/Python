# oops = object oriented programmings

# class is a blueprint of an object
# object is an instance of a class

# class contains data members and member functions
class Number:                           # here Number is a class
    def sum(self):                      # here sum is a member function
        return self.a + self.b          # here a and b are data members
    
    def sub(self):
        return self.a - self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
d = num.sub()
print(s)
print(Number.sum(num))
print(d)

# a = 12
# b = 34

# print("The sum of a and b is ", a+b)

'''
PascalCase 
EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''