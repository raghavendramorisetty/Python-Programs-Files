#FilterFunEx2.py
iseven=lambda n :  n%2==0  # Anonymous Function

#Main program
print("Enter List of Values Separated by Space:")
lst=[int(val) for val in input().split()] # lst=[11,12,13,14,16,17]
evenlist=list(filter(iseven,lst))
print("Given List={}".format(lst))
print("Even List={}".format(evenlist))