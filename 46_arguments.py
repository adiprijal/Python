# This script explains about the arguments in python

# Default Arguments
def greet(name="Stranger"):                 # here, we set 'Stranger' as the default argument of our function
    print("Good Day, "+ name)
 

greet("Adip") 
greet()


# Keyword Arguments
    # >>> You can also send arguments with the key = value syntax.
def greet(name, msg):
    print("Hello", name + ', ' + msg)

greet(msg = "Good Morning" , name = "Adip")         # Here, the order of the arguments does not matter.


# Arbitrary Arguments
    # >>> If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def greet(*names):
    for name in names:
        print("Hello", name)
        print("Hello", names[2])        # Accessing the elements of the list

greet("Adip", "Shishir", "Manoj", "Kiran")


# Arbitrary Keyword Arguments
    # >>> If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def greet(**names):
    for key, value in names.items():
        print(key, value)
names = {"name1":"Adip", "name2":"Raj", "name3":"Kumar", "name4":"Ravi"}
greet(**names)
# greet(name1="Adip", name2="Raj", name3="Kumar", name4="Ravi")


# Order of Arguments
    # >>> The order of the arguments is important. You must pass the values in the order the arguments are declared.
def greet(name, msg):
    print("Hello", name + ', ' + msg)

greet("Adip", "Good Morning")
# greet("Good Morning", "Adip")       # This is an error input