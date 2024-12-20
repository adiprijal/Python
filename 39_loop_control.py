for a in range (1,11):
    print(a)
else:
    print('Time up..')


for i in range(1,11):
    if i==5:
        continue                # >>> skips 5
    if i==8:
        break                   # >>> terminates at 8
    print(f'Now i is {i}')