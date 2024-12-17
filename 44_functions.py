# marks1 = [45, 78, 86, 77]
# percentage1 = (((marks1[0] + marks1[1] + marks1[2]+ marks1[3])/400 )*100)
# marks2 = [75, 98, 88, 78]
# percentage2 = ((marks2[0] + marks2[1] + marks2[2]+ marks2[3])/400 )*100
# print(percentage1, percentage2)


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