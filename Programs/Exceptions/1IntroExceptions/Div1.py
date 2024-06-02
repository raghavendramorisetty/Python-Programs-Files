#Program for Calculating Division of Two Numbers
#Div1.py
print("Program Execution Started")
s1=input("Enter First Value:")
s2=input("Enter Second Value:")
#convert s1 and s2 into int type
a=int(s1)#-----------------------------Exception generated stmt--ValueError
b=int(s2)#-----------------------------Exception generated stmt--ValueError
print("Val of a={}".format(a))
print("Val of b={}".format(b))
#do the div
c=a/b #--------------------------------Exception generated stmt---ZeroDivisionError
print("Div={}".format(c))
print("Program Execution Ended")
