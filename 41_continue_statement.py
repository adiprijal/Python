for a in range (10):
    if 5<=a<8:
        # print(a)      >>> 6,7
        continue      # >>> continue loop ignoring 5<=a<8
    print(a)


# to print even numbers
for b in range (40):
    if b%2!=0:          # >>> '!=' means not equal to
        continue
    print(b)            # >>> prints even numbers from 0 to 39


# to print odd numbers
for b in range (40):
    if b%2==0:
        continue
    print(b)            # >>> prints odd numbers from 0 to 39


# to print factors of a number
num = int(input("Enter the number:\n"))
f=[]
for fac in range (1,num+1):
    if num%fac==0:
        f.append(fac)
print(f'Factors of {num} are {f}')