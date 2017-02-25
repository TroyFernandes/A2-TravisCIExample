def Half(value):
    return value/2

def Quarter(value):
    return value/4

def Divide(value,divisor):
    if divisor == 0:
        raise ZeroDivisionError('The divisor cannot be zero')
    return  value / divisor

