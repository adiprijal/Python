joke = "eka desh ma euta budo thyo,,tyo bachhai ma moryo."

# String Functions
print(len(joke))       # len=lenght of string

print(joke.endswith("."))
print(joke.endswith("moryo."))
print(joke.endswith("hi"))

print(joke.count("a"))
print(joke.count("yo"))
print(joke.count("desh"))
print(joke.count(","))

print(joke.capitalize())    #capitalize 1st character

print(joke.find("ma"))      # find the index of 1st occurenceof characters
print(joke.find("adip"))    # -1 = doesn't exist
print(joke.find("eka"))

print(joke.replace("ma","maa"))  #replace all "ma" with "maa"

a="Adip"
b="54657"
c="Adip Rijal"              
print(a.isdigit())          # >>>False
print(b.isdigit())          # >>>True
print(c.isdigit())          # >>>False

print(a.isalpha())          # >>>True
print(b.isalpha())          # >>>False
print(c.isalpha())          # >>>False

