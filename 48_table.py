import datetime

year = datetime.datetime.now().year
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute


table = {'Year': year, 'Hour': int(hour), 'Minute': int(minute)}
print (F'The datatype of table variable is {type(table)}')                       # The datatype of table variable is <class 'dict'>

print ('The datatype of table.items() is {}'.format(type(table.items())))           # The datatype of table.items() is <class 'dict_items'>

for i,value in table.items():
    print(f'{i:10}-{value:10d}')     # Passing an integer after ':' will cause that field to be minimum number of characters wide.

# Here 10d means that the integer value will be printed in a field of width 10 characters. If the integer value is less than 10 characters wide, it will be padded with spaces.
# 10d indicates that the output is treated as a decimal integer number.
# If you use 10d and the value is not a number, you will get a TypeError.


# 10s indicates that the output is treated as a string of characters.
# 10f indicates that the output is treated as a floating point number.
# 10.2f indicates that the output is treated as a floating point number with 2 decimal places.
# 10.2s indicates that the output is treated as a string of characters with a minimum width of 10 characters and a maximum width of 2 characters.
# 10.2d is invalid because the 'd' format specifier is only for integers.