# pass is used to continue without doing anything{without executing}
# function lekhne tara execute nagarne

for a in range (10):
    if 5<=a<8:
        pass
    else:
        print(a)


# to print even numbers
for b in range (40):
    if b%2!=0:
        pass
    else:
        print(b)        # >>> prints even numbers from 0 to 39


# We use pass statement to write empty loops. Pass is also used for empty control statements, functions, and classes.
# Pass is a null statement in Python. Nothing happens when it is executed. It is used as a placeholder.
# We can use pass when we have a block of code that is not implemented, but we want to implement it in the future.
# It is used to prevent indentation errors and indicates that no action is to be taken.