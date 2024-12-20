for a in range(10):         # >>> range 0-9
    print(a)                # >>> prints 0-9

for b in range(5,15):       # >>> range 5-14
    print(b)

for c in range(6,24,2):      # >>> range 6-23
    print(c)                 # >>> prints every 2nd{**gap of 1 num} number from 6 to 23


num = range(10)
print(num)                  # >>> prints range(0,10)
print(list(num))            # >>> prints [0,1,2,3,4,5,6,7,8,9]  # >>> converts range to list
print(num[5])               # >>> prints 5

num2 = range(5,15)
print(num2)                 # >>> prints range(5,15)
print(num2[5])              # >>> prints 10