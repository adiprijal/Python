import random

print(random.randint(1,10))
print(random.random())              # between 0 and 1

l=['rock','paper',"scissors"]
print(random.choice(l))

cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
random.shuffle(cards)
print(cards)