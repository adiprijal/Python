'''{and} operator'''
# Both the conditional should be fulfilled
marks=int(input('Enter your marks:\n'))
if marks>=80 and marks<90:
    print('A')
else:
    print('Not A')

'''{or} operators'''
# at least one conditional should be fulfilled
age=int(input("Enter your age:\n"))
if age <= 14 or age > 65:
    print("You belong to dependent population")
else:
    print("You belong to independent population") 

'''{not} operator'''
# gives opposite result
age=int(input("Enter your age:\n"))
if not age<45 :
    print("Negative result")