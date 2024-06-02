#AnonymousFunEx5.py
findmax=lambda lst:max(lst)
findmin=lambda lst:min(lst)
#Main Program
print("Enter List of Numerical Values Separated by space:")
lst=[int(val) for val in input().split()]
maxv=findmax(lst)
minv=findmin(lst)
print("Max({})={}".format(lst,maxv))
print("Min({})={}".format(lst,minv))