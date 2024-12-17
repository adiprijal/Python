def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Invalid value..increment number hunxa jpt nalekh..")

a = increment("5445d")
print(a)