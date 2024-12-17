a=set()             # >>> a is a empty set
print(type(a))      # >>> class 'set'

a.add(1)
a.add(1)
a.add("5")
a.add("z")
a.add((2,3,4))      # >>> can add a tuple
# b.add([3,6,8])    # >>> cannot add a list
# a.add({4:7})      # >>> cannot add a dict.
print(a)

a.remove("z")       # >>> removes 'z' from the set
# a.remove(435)     # >>> *error {435 is not in the set}
print(a)

print(len(a))

print(a.pop())      # >>> remove a random element from set
print(a)            # >>> print set removing the popped element

a.clear()
print(a)

b = {1,3,5,7,9,11,13,15,17,19}
c = {2,3,5,7,11,13,17,19}
d = b.union(c)
e = b.intersection(c)
print(d)
print(e)