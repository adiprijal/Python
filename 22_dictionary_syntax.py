dict={
    "greeting":"Good Morning",
    "game":"sports",
    "number":143,
    "digits":[0,1,2,3,4,5,6,7,8,9],
    "new.dict":{"code":"python"},
    1+1:65
}

print(dict['greeting'])
print(dict['number'])
print(dict['digits'])
print(dict[1+1])

dict['game']=["exercise"]
print(dict['game'])

print(dict)
print(dict['new.dict'])
print(dict['new.dict']['code'])