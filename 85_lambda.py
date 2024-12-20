# This is a function.
def func(a):
    return a+5


# This is a lambda function.
    # >>> lambda function is a small anonymous function.
    # >>> A lambda function can take any number of arguments, but can only have one expression.
    # >>> Syntax: lambda arguments : expression
func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6