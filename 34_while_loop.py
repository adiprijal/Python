'''While loop'''

a = 1
while a<10:
    print('Yes',a)
    a=a+1               # >>> gives 9 'yes'

# a=0
# while a<=1000:
#     print(a)
#     a=a+1             >>> prints 0 to 1000


while True:
    print('Enter a number')
    num = int(input())
    if num>100:
        print('Congrats you have entered a number greater than 100')
        break

''' 
    >> Infinite loop <<

while True:
    print('Yes')        # >>> infinite loop

'''