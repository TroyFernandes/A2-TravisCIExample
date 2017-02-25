import Multiplication
import Division
valueData = [8, 3, 0.52, 0.72, 0, 95, 0.5, 16, 6, 0.26, 331, 123.1, 0]

def TestCode(data):
    for number in data:
        if number == 0:
            print("Skipping over value 0\n")
            continue
        try:
            print("{0} squared is {1}\n".format(number,Multiplication.Square(number)))
            print("{0} cubed is {1}\n".format(number,Multiplication.Cube(number)))
            print("{0} multiplied by 3 is {1}\n".format(number,Multiplication.Multiply(number,3)))
            print("{0} halved is {1}\n".format(number,Division.Half(number)))
            print("{0} quartered is {1}\n".format(number,Division.Quarter(number)))
            print("{0} divided by zero is {1}\n".format(number,Division.Divide(number,0)))
        except ZeroDivisionError:
            print("Divisor cannot be zero\n")

