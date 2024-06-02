#AnonymousFunEx1.py
sumop=lambda a,b:a+b

#Main program
print("Type of sumop=",type(sumop))  # <class 'function'>, Hence sumop is object of type <class 'function'>, can be used for function call
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
res=sumop(a,b)
print("sum({},{})={}".format(a,b,res))