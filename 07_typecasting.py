# 143 is a numeric literal & "143" is a string literal
# int:integer   str:string   float:floating integer   bool:boolean

a = 143
print(type(a))
a = "143"
print(type(a))

a=143           #143 is a integer
print(type(a))
a=float(a)      #float typecast change a variable to FLOATING number
print(a)
print(type(a))

a="143"    #143 is a string
a=int(a)   #int typecast change a variable to integers varible
print(type(a))

a=143    #143 is a integer variable
a=str(a)   #str typecast change a variable to string varible
print(type(a))

a = "False"     #False is a string
print(type(a))
a = bool(a)     #bool typecast change a variable to booleans
print(type(a))

n=234
print(complex(n))


# Complex number can't be typecasted to int or float
c = 3 + 0j
print(str(c))           
print(type(str(c)))     
print(int(c))           # Error
print(float(c))         # Error