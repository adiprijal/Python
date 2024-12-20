dict={
    "greeting":"Good Morning",
    "game":"sports",
    "number":143,
    "digits":[0,1,2,3,4,5,6,7,8,9],
    "new.dict":{"code":"python"},
}

del dict["game"]                # del deletes the key and value from dictionary.
print(dict)

print(dict.keys())                  # keys() returns all the keys of the dictionary.
print(list(dict.keys()))            # list() converts the keys into list.
print(tuple(dict.keys()))           # tuple() converts the keys into tuple.
# print(type(dict.keys()))       >>> class 'dict_keys'

print(dict.values())                # values() returns all the values of the dictionary.
print(list(dict.values()))

print(dict.items())                 # items() returns all the key-value pairs of the dictionary.

new_dict = {
    1+1 : 34, "red":"colour",
    "greeting": "Namaste"
}

dict.update(new_dict)               # update() adds the new dictionary to the existing dictionary.
print(dict)

# print(dict['game'])               >>> sports
# print(dict.get('game'))           >>> sports {same}
# print(dict['game2'])              >>> *error  [game2 is  not in the dict]
# print(dict.get('game2'))          >>> none    [game2 is  not in the dict]


dict.pop('number')              # pop('key') deletes that key and value from dictionary.
print(dict)

dict.popitem()                  # popitem() deletes last key and value from dictionary.