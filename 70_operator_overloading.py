class Number:
    def __init__(self,num1):
        self.numr=num1

    def __add__(self,num2):
        print("ADD")
        return self.numr+num2.numr
    
    def __sub__(self,num2):
        print("SUBTRACTION")
        return self.numr-num2.numr
    
    def __mul__(self,num2):
        print("MULTIPLY")
        return self.numr*num2.numr
    
    def __truediv__(self,num2):
        print("DIVISION")
        return self.numr/num2.numr
    
    def __floordiv__(self,num2):
        print("DIVISION(float)")
        return self.numr//num2.numr

n1=Number(25)
n2=Number(8)
sum=n1+n2
print(sum)
sub=n1-n2
print(sub)
mul=n1*n2
print(mul)
div=n1/n2
print(div)
floordiv=n1//n2
print(floordiv)