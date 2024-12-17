try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")        # >>>Finally compulsorily get printed.

print("Thanks for using the program")