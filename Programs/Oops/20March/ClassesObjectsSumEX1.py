#Program for adding of Two Numbers by using Classes and Object
#ClassesObjectsSumEX1.py
class Add:pass

#Main Program
o1=Add()
o1.a=float(input("Enter First Value:"))
o1.b=float(input("Enter Second Value:"))
#add them
o1.c=o1.a+o1.b
print("sum({},{})={}".format(o1.a,o1.b,o1.c))