# marks1 = [45, 78, 86, 77]
# percentage1 = (((marks1[0] + marks1[1] + marks1[2]+ marks1[3])/400 )*100)
# marks2 = [75, 98, 88, 78]
# percentage2 = ((marks2[0] + marks2[1] + marks2[2]+ marks2[3])/400 )*100
# print(percentage1, percentage2)


# Function 1
def percent(marks):
    # return (sum(marks)/400)*100
    p = (sum(marks)/400)*100
    return p

marks1 = [45, 78, 86, 77]
per1 = percent(marks1)

marks2 = [75, 98, 88, 78]
per2 = percent(marks2)

marks3 = [56, 68, 39, 45]
per3 = percent(marks3)
print(f"{per1}%, {per2}%, {per3}%")


# Function 2
def greet(name):
    print('Good Day,'+name+'...')

name=input('Enter your name:\n')
greet(name)


# Function 3
def circumferenceOfCircle(r):
    circumference = 2 * (22/7) * r
    print ('The circumference of circle is {}.'.format(circumference))

circumferenceOfCircle(5)
circumferenceOfCircle(7)
circumferenceOfCircle(9)