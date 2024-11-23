
def add(a, b):
    return a+b



def mul(a,b):
    return a*b



def subt(a,b):
    return a-b



def div(a,b):
    if b == 0:
        raise ValueError("can not divide by zero")
    return a/b
