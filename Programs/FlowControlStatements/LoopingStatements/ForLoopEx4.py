#Program for Obtaining sum of Digits of Given Number
#ForLoopEx4.py
num=input("Enter A Number:") # num=2378
s=0
for val in num:
    s=s+int(val)
else:
    print("SumOfDigits({})={}".format(num,s))
print("----------------OR--------------------------")
s=0
for val in num[::-1]:
    s=s+int(val)
else:
    print("SumOfDigits({})={}".format(num,s))
print("----------------OR--------------------------")
s=0
n=int(num)#Converting str num type into int type--n=2378
tn=n # Here tn is Temp Var which holds Original Value
while(n>0):
    r=n%10#gets remainder
    s=s+r
    n=n//10
else:
    print("Sum({})={}".format(tn,s))