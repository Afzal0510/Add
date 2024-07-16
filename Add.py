def str_to_int(func):
    def wrapper(a,b):
        a,b=int(a),int(b)
        return func(a,b)
    return wrapper

@str_to_int
def AddTwoNumber(a,b):
    return a+b
a,b="3",4
print("Sum = ", AddTwoNumber(a,b))
