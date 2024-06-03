# Program for Defining  for Cal Square Root of Value returned by Normal Function by using Decorator
# DecEx1.py

def getval():  # Here getval() defined by KVR
    return float(input("Enter Numerical Value:"))


def squareroot(gv):
    def operation():
        n = gv()
        res = n ** 0.5
        return n, res
    return operation


# main program
op = squareroot(getval)  # Decorator Function call
n, result = op()
print("SquareRoot({})={}".format(n, result))
