# Format 1
a = 'Python';  b = 'programming'
print('{} is incredibly versatile {} language.'.format(a,b))

# output = 'Python is incredibly versatile programming language.'

# Format 2
print('We will be {1} in {0}.'.format(a,b))

# output = 'We will be programming in Python.'

# Format 3
print('We will be {place1} machine learning {place2}.'.format(place1 = 'learning',place2 = 'concepts'))

# output = 'We will be learning machine learning concepts.'

# Format 4
message = input('Enter a departing message\t')
print('Eveyone please be seated.',message)

# output = 'Everyone please be seated. >user input<'

print(f'{a} is incredibly versatile {b} language.')