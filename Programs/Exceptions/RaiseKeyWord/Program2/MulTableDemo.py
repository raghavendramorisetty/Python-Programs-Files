#MulTableDemo.py------Main Program
from MulTabExceptions import ZeroError,NegNumError
from MulTable import table
try:
    n = int(input("Enter a Number for generating Mul table:"))
    table(n) # Function call--Result  and Exception
except ZeroError:
    print("\tDON'T ENTER ZERO FOR MUL TABLE")
except NegNumError:
    print("\tDON'T ENTER NEGATIVE NUMBER FOR MUL TABLE")
except ValueError:
    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except:
    print("Some thing went wrong")


