    # doesn't require close function
with open('sample.txt','r') as t:
    d=t.read()
with open('sample.txt','a') as t:
    d=t.write(".......")
print(d)