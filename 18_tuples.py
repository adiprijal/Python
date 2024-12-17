# values in list can be changed but not in tuple

# t=()
# t=(1,)                #single element tuple needs comma
t=(1,2,3,4,5)
print(t)
print(t[-1])

# t[3]=8    {wrong}values can't be changed