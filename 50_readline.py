    # using readline function

try:
    f = open('sample.txt')
    data=f.readline()           # reads first line
    print(data)
    data=f.readline()           # reads second line
    print(data)
    f.close()
except FileNotFoundError:
    print("File not found!")