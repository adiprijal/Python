# List Comprehension
a = [2, 3, 4, 6, 7, 8, 9, 13, 23, 67, 75, 123]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

b=[i for i in a if i%2==0]
print(b)


# Even number list using list comprehension
even = [i for i in range(100) if i%2==0]
print(even)


# Set Comprehension
list=[1,4,2,54,4,3,8,3,8]
set={i for i in list}           
print(set)


# Dictionary Comprehension
dict={i:f"item{i}" for i in range(1, 11)}
print(dict)


# Tuple Comprehension
tuple=tuple((i for i in range(1, 101) if i%2==0))
print(tuple)



# Lambda Comprehension
add=[(lambda a=i:a**2)(i) for i in range(1, 11)]
print(add)

minValue = lambda num1, num2 : num1 if num1 < num2 else num2
print ('The minimum value is',minValue(5, 6),'.')