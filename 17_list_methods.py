l1=["a","d","sg","f"]
l1.sort()                         # only single data type works...
                                    # l1=["a",32,2.5,"d",0,"sg","f"]   {doesn't work}
l1.reverse()
l1.append("adip")     # adds a value at the end of list{one only}
l1.append("rijal")
l1.append(143)
l1.insert(0,6)        #(index,new value) : add a new value at a index.  
l1.insert(24,"ag")    # if the index no is more than last no of values , new value is added at the last of the list
l1.pop(2)             # delete one value at given index
l1.remove("sg")       # remove a value  
print(l1)

l2=[5,8,65,4,45.5,5]
l2.sort()
l2.reverse()
l2.append(143)
l2.append("rijal")
l2.insert(-1,"adip")
l2.pop(-2)
l2.remove(65)
print(l2)

a= [1,2,3,5,8,25,2,14,5]
print(a[0]+a[2]+a[5]+a[7])
print(sum(a))