str = "a:1,b:2,c:3"
# dict1 = dict(str)                 # TypeError: 'str' object is not callable
pairs = str.split(',')              # split() converts the string into list.
print(pairs)                        # ['a:1', 'b:2', 'c:3']

# Method 1 
dict1 = dict(pair.split(':') for pair in pairs)    # dict() converts the list into dictionary.
print(dict1)                        # {'a': '1', 'b': '2', 'c': '3'}

# Method 2 
Dict2 = {}
for pair in pairs:
    key, value = pair.split(':')
    print('The key is :',key)
    print('The value is :',value)
    Dict2[key] = int(value)
print(Dict2)                        # {'a': 1, 'b': 2, 'c': 3}