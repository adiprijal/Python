    # doesn't require close function
with open('sample.txt','r') as t:  
    d=t.read()                      # ou
with open('sample.txt','a') as t:
    t.write(".......")
print(d)