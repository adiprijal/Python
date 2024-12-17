a= 55               # Global Variable
def func():
    global a
    print (a)       # >>> prints a=55
    a=24            # change global variable
    print(a)

func()
print(a)