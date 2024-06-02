#Program for Finding Bigegst Two Numbers and Check for Equality
#FindBigTwoEx2.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
#Find  Big
big=a if a>b else b if b>a  else "Both Values are Equal"
print("Big({},{})={}".format(a,b,big))