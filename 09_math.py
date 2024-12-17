import math
# help('math')

# division of two int gives float
print(10/2)

print(10/3)
print(10//3)                        # Floor division

print(math.ceil(10/3))              # Round up
print(math.floor(10/3))             # Round down

# Precedence of operators

# Parentheses                                       ()
# Exponentiation                                    **
# Division, Floor Division, Modulus, Multiplication /, //, %, /
# Addition, Subtraction                             +, -


# Division, Floor Division, Modulus, Multiplication, Add, Subtract     left to right

# Exponetiation (**)              right to left

print(2**3**2)              # ans= 512