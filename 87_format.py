name = "Adip"
country = "Nepal"
type = "home"
a = f"I am {name}"
print(a)
a = "I am {}".format(name)
print(a)
a = "I am {} and my country is {}.".format(name, country)
print(a)
a = "I am {} and my {} country is {}.".format(name, type, country)
print(a)
a = "I am {0} and my {2} country is {1}.".format(name, country, type)

print(a)