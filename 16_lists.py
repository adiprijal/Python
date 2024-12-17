a = ["z", "y", 1, 2, "w", True, False, 143.3]
print(a)
print(a[0])
print(a[5])
print(a[-4])

# exchanging values
a[1]="a"
a[5]=None
print(a)

# slicing
print(a[2:6])
print(a[:-1:3])
print(a[::2])


# 2D lists (list of lists)
a=["abs","hi","hello"]
b=[32,53,"Apple",True]
c=["add",36,False,None,56.376]

z=[a,b,c]
print(z)
print(z[0])
print(z[1])
print(z[2])
print(z[0][2])      # index 2 element of z[0] list
print(z[1][3])
print(z[2][2])