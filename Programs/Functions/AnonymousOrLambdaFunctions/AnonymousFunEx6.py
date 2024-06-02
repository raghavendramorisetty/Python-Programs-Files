#AnonymousFunEx6.py
arrange=lambda lst,val: sorted(lst) if val=="asc" else sorted(lst)[::-1]
#Main Program
print("Enter List of Numerical Values Separated by space:")
lst=[int(val) for val in input().split()]
res1=arrange(lst,"asc")
res2=arrange(lst,"desc")
print("Ascending Order=",res1)
print("Decending Order=",res2)
