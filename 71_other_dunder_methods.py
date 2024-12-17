class Number:
    def __init__(self, num):
        self.num = num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    def __len__(self):
        return len(str(self.num))

n = Number(96565)
print(n)
print(len(n))