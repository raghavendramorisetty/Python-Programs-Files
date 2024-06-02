upper=lambda n: n.swapcase()
#Main Program
print("Enter List of words Separated by Space:")
lst=[val for val in input().split()]
upperlist=tuple(map(upper,lst))
print("Given List=",lst)
print("Upper Case List=",upperlist)