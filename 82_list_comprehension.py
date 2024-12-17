a = [2, 3, 4, 6, 7, 8, 9, 13, 23, 67, 75, 123]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

b=[i for i in a if i%2==0]
print(b)


l=[1,4,2,54,4,3,8,3,8]
s={i for i in l}            # set comprehension
print(s)