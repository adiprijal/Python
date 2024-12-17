dict={
    "greeting":"Good Morning",
    "game":"sports",
    "number":143,
    "digits":[0,1,2,3,4,5,6,7,8,9],
    "new.dict":{"code":"python"},
}

print(dict.keys())
print(list(dict.keys()))
print(tuple(dict.keys()))
# print(type(dict.keys()))       >>> class 'dict_keys'

print(dict.values())
print(list(dict.values()))

print(dict.items())

new_dict = {
    1+1 : 34, "red":"colour",
    "greeting": "Namaste"
}
dict.update(new_dict)
print(dict)

# print(dict['game'])               >>> sports
# print(dict.get('game'))           >>> sports {same}
# print(dict['game2'])              >>> *error  [game2 is  not in the dict]
# print(dict.get('game2'))          >>> none    [game2 is  not in the dict]
