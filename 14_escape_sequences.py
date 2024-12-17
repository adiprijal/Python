# Example: \ ,\\ ,\' ,\" ,\a ,\b ,\f ,\n ,\r ,\t ,\v ,\{octal number} ,\x{hex. value} ,\N{{character name}}  etc


# https://www.python-ds.com/python-3-escape-sequences

Hi = "Adip is a very good boy.\nHe \nis \ta so\rjo manxe."
print(Hi)

print("I \
am \
Adip")        # \ is used to use multiple line

print("I am \nAdip")   # \n = to change line

# print("\")  doesn't print \
print("\\")    #prints \
print("\\\ ")

# print('I said,"Hi". He's a boy.')
print('I said,"Hi". He\'s a boy.')
# print("I said,"Hi". He's a boy.")
print("I said,\"Hi\". He's a boy.")
# print('''I said,"Hi". He's a''' boy.''')
print('''I said,"Hi". He's a\''' boy.''')

print("\a")
print("I am \b Adip.")
print("Hi \f everyone.")  # to insert ♀ symbol
print("Hi \v everyone.")  # to insert ♂ symbol
print("Hi \n everyone.")
print("Hi \r everyone.")
print("Hi \t everyone.")

print("\110\145\154\154\157")  # \*** octal value
print("\x48\x65\x6c\x6c\x6f")  # \x** hexadecimal value



