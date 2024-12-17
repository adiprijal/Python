import m78_file1 as m1
m1.greet("Adip")


from m78_file1 import greet,hi
greet("Adip")
hi()

from m78_file1 import *
greet("Adip")
hi()