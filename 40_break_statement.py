for a in range (10):
    if a>5:             # >>> loop breaks at 6
        break
    print(a)
else:
    print('Done')       # >>>else doesn't execute {**break}


# Break statement
count = 0

while True:
    print(count)
    count += 1
    if count >= 5:
        break
