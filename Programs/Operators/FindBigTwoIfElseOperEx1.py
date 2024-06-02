#Program for Finding Bigegst Two Numbers and Check for Equality
#FindBigTwoEx1.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
#Find  Big
big=a  if a>b else b
print("Big({},{})={}".format(a,b,big))