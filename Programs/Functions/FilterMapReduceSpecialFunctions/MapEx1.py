#MapEx1.py
def square(n): # Normal Function
    return (n**2)

#Main Program
print("Enter List of Values Separated by Space:")
lst=[int(val) for val in input().split()] # lst=[11,12,13,14,16,17]
obj1=map(square,lst)
print("Type of obj1=",type(obj1))  #  <class 'map'>
#Convert Map object into List object
sqlist=list(obj1)
print("Given List=",lst)
print("Square List=",sqlist)