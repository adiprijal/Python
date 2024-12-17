'''if else ladder'''

# if(cond.)..elif(cond.)..elif(cond.).....else(cond.)
# only one program is executed

a = 35
if (a>45):
    print('The value of a is greater than 45')
elif(a==35):
    print('The value of a is equal to 35')
elif(a>19):
    print('The value of a is greater than 19')
elif(a>87):
    print('The value of a is greater than 87')
else:
    print('The value of a is not greater than 45 or 34 or 19 or 87')


'''multiple if statements'''
# all true statement/s are executed
# if(cond.)..if(cond.)..if(cond.).....if(cond)..else(cond.)

a=37
if(a>45):
    print('The value of a is greater than 5')
if(a>34):
    print('The value of a is greater than 34')
if(a>19):
    print('The value of a is greater than 19')
if(a>7):
    print('The value of a is greater than 7')       # if_else statement starts from here
else:
    print('The value of a is not greater than 45 or 34 or 19 or 87')