#MapEx2.py
square=lambda n: n**2
#Main Program
print("Enter List of Values Separated by Space:")
lst=[int(val) for val in input().split()] # lst=[11,12,13,14,16,17]
sqlist=tuple(map(square,lst))
print("Given List=",lst)
print("Square List=",sqlist)