#Concatenating

hi="Good"
hello="morning"
print(hi+hello)
c=hi+hello
print(c)
print(hi,hello)

# indexing a string..example
# m  o  r  n  i  n  g
# 0  1  2  3  4  5  6
#-7 -6 -5 -4 -3 -2 -1

print(hi[3])
print(hello[2])
print(hello[-4])

print(hello[0:4])    # last limit is excluded i.e. 0 1 2 3
print(hello[3:7])    # it includes indexes 3 4 5 6
print(hello[-5:-2])    # -5 -4 -3
print(hello[:7])      #[:7] = [0:7]
print(hello[-6:])     #[-6:]= [-6:-1]

# Skip slicing
a="AdipRijal"
print(a[0:6:1])   #[start:end:skip value]   1= no skip
print(a[0:6:2])   # 2 = skip every 1 digit
print(a[0::3])    # 3 = skip every 2 digit

# print(hello[6:3])
# print(hello[-2:-5])  it doesn't work from backward