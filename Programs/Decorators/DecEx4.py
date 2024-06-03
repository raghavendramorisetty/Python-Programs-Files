# Program for Defining  for Calc Square and Square Root of Value returned by Normal Function by using Decorator
# DecEx4.py
def square(sqrt):
    def operation():
        n, sqrtres = sqrt()
        sqrres = n ** 2
        return n, sqrtres, sqrres

    return operation


def squareroot(gv):
    def compute():
        n = gv()
        sqrtres = n ** 0.5
        return n, sqrtres

    return compute


@square
@squareroot
def getval():  # Here getval() defined by KVR
    return float(input("Enter Numerical Value:"))


# Main Program
gn, sqrtresult, sqrresult = getval()  # Normal Function Call or We can use   "square(squareroot(getval))()"   if @ symbol of decorators in line 21 and 22 are not used..shown below
print("SquareRoot({})={}".format(gn, sqrtresult))
print("Square({})={}".format(gn, sqrresult))



# OR
#
# def square(sqrt):
#     def operation():
#         n, sqrtres = sqrt()
#         sqrres = n ** 2
#         return n, sqrtres, sqrres
#
#     return operation
#
#
# def squareroot(gv):
#     def compute():
#         n = gv()
#         sqrtres = n ** 0.5
#         return n, sqrtres
#
#     return compute
#
#
# #@square
# #@squareroot
# def getval():  # Here getval() defined by KVR
#     return float(input("Enter Numerical Value:"))
#
#
# # Main Program
# gn, sqrtresult, sqrresult = square(squareroot(getval))()
# print("SquareRoot({})={}".format(gn, sqrtresult))
# print("Square({})={}".format(gn, sqrresult))
