#FilterFunEx3.py
print("Enter List of Values Separated by Space:")
lst=[int(val) for val in input().split()] # lst=[11,12,13,14,16,17]
evenlist=list(filter( lambda n:n%2==0 , lst))
print("Given List={}".format(lst))
print("Even List={}".format(evenlist))