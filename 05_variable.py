# a,b,c,d,e... are variables data
# variables contains values (strings,integers,dot floating numbers,booleans,none,complex,array and others)

a = 'string'
A = "string"
b = "also string"
c = '''also string too'''
d = '''string
in multiple
line
'''

# a,b,c,d are string variables.
'''
strings as a value are written between single quote('_')
but double(") and triple(' ' ')quote can also be used 
,if double is included in the string as a value
'''
# strings in triple quote can be written in multiple line example;


e = 143
f = 143.3
# e is 'integer variable' and f is 'dot floating integer'


g = True
h = False
# True and False are 'booleans

i = None
# None refers for nothing :)


# printing the variables
print(a)
print(A)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

''' Rules for writing variables '''
# Variable name can contain alphabets,numbers and underscore
a_1 = "Rule 1"
print(a_1)
# Variable name can't start with number but can start with alpha. & numb,.
     #Ex: 1 = (one) & 1a = (one-a) are invalid

# BlankSpace is not allowed..
    # Ex: ar 4 =(Hi) is invalid  but ar_4 = (Bye) is valid

# They are case-sensetive

"multiple assignment"
a,b,c=23,"Adip",True
print(a)
print(b)
print(c)


j = 2 + 5j
# j is a complex number variable


print(j)
print(type(j))

print(j.real)               # real part of complex number j
print(j.imag)               # imaginary part of complex number j
print(j.conjugate())        # conjugate of complex number j

# Complex constructor
z = complex(3, 4)  # Equivalent to 3 + 4j
print(z)           # Output: (3+4j)


print(type(z))           # Output: <class 'complex'>
print(isinstance(z, complex))  # Output: True