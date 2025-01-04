    # using open function

# # f = open('sample.txt', 'r')
f = open("sample.txt")          # read is a default function

# opening file in write and read mode
# f = open("sample.txt", "w+")

# add content to the file
# f.write("Hello World.\n")
# f.write("This is our new text file.")

# read content from the file
    # opening file in read mode, you can only read certain amount of characters only once
    # ex: you read the file using f.read() and then you can't read it again using f.read() unless you close the file and open it again. Using f.read() twice will return empty string

# print(f.read())
print(f.read(6))                 # >>> prints the first 6 characters of the contents
print(f.readline())              # >>> prints the first line of the contents
# you can read 2nd line by using f.readline() again
print(f.readline())              # >>> prints the second line of the contents

print(f.readlines())             # >>> prints the contents in a list format


# reading file using loop
f = open("sample.txt")
for a in f:
    print(a, end='')         # end='' is used to remove the extra line

# closing the file
f.close()


'''
+ = updating mode
w = write mode
a = append mode
r+ = read and write mode
w+ = write and read mode
a+ = append and read mode
x = exclusive creation
rb = open for read in binary mode
r or rt = open for read in text mode
'''


#  Appending to a file
f = open("sample.txt", "a")
f.write("This is the appended text.")
f.close()


#  Writing to a file
f = open("sample.txt", "w")
f.write("f.write overwrite the content. \nThis is the new text. \n")
f.close()

# import os
# path="C:\\Users\\rizal\\Desktop\\Adip.psd"

# if os.path.exists(path):
#     print("Exists.")
#     if os.path.isfile(path):
#         print("Is a file.")
#     elif os.path.isdir(path):
#         print("Is a directory.")
# else:
#     print("Doesn't exists.") 