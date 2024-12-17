print("Press q to quit..")
while True:
    a=input("Enter a number:\n")
    if a=="q":
        break
    try:
        a=int(a)
        if a>55:
            print("You entered a number greater than 55.")
        elif a==55:
            print("You entered pachpanna.")
        else:
            print("You entered a number smaller than 55.")
    except Exception as e:
        print(f"**Your input is invalid.")

print("Thank you!!")