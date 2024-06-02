#FilterFunEx4.py
print("Enter List of Numerical values Separated by space:")
lst=[int(val) for val in input().split()]
poslist=list(filter( lambda num:num>0 , lst))
neglist=list(filter( lambda num:num<0 , lst))
print("Given List of words={}".format(lst))
print("Poslist List={}".format(poslist))
print("neglist List={}".format(neglist))