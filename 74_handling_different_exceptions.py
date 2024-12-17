while True:
    try:
        a = input("Enter a number: ")
        if a=="quit":
            break
        a=int(a)
        c = 1/a
        print(f"The reciprocal of {a} is {c}.")

    except ValueError as e:
        print("Please! , Enter a valid value") 

    except ZeroDivisionError as e:
        print("Make sure you are not dividing by 0") 

print("Thanks for using this code!")