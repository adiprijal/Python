    # using open function

# # f = open('sample.txt', 'r')
f = open('sample.txt')          # read is a default function
# data=f.read()                 # >>> prints the contents of the file
data=f.read(6)                 # >>> prints the first 6 characters of the contents
print(data)
f.close()


'''
+ = updating mode
rb = open for read in binary mode
r or rt = open for read in text mode
'''

import os
path="C:\\Users\\rizal\\Desktop\\Adip.psd"

if os.path.exists(path):
    print("Exists.")
    if os.path.isfile(path):
        print("Is a file.")
    elif os.path.isdir(path):
        print("Is a directory.")
else:
    print("Doesn't exists.") 