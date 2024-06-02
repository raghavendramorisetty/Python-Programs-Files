# FilterFunEx1.py
def iseven(n):  # Normal Function
    if (n % 2 == 0):
        return True
    else:
        return False


# Main program
print("Enter List of Values Separated by Space:")
lst = [int(val) for val in input().split()]  # lst=[11,12,13,14,16,17]
obj1 = filter(iseven, lst)
print("type of obj1=", type(obj1))  # <class 'filter'>
# Convert Filter Object into tuple
evenlist = tuple(obj1)
print("Given List={}".format(lst))
print("Even tuple={}".format(evenlist))
