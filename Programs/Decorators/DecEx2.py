# Program for Defining for Calculate Square Root of Value returned by Normal Function by using Decorator
# DecEx2.py

def getval():  # Here getval() defined by KVR
    return float(input("Enter Numerical Value:"))


def squareroot(gv):
    def operation():
        n = gv()
        res = n ** 0.5
        return n, res

    return operation


# Main program
n, result = squareroot(getval)()  # Decorator Function Call
print("SquareRoot({})={}".format(n, result))
