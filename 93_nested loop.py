rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end='')
    print()