try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We were successful")


try:
    i = int(input("Enter a number: "))
    c = 1/i
    print("We were successful")
except Exception as e:
    print(e)
else:
    pass