#program for Calculating Simple Interest and total amount to pay
#ArithmeticOperatorsEx2.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
#calculate si and totamt
si=(p*t*r)/100
totamt=p+si
#dispplay the result
print("="*50)
print("Simple Interest Calculation")
print("="*50)
print("\tPrinciple Amount:{}".format(p))
print("\tTime:{}".format(t))
print("\tRate of Interest:{}".format(r))
print("-"*50)
print("\tSimple Interest:{}".format(si))
print("\tTOTAL AMOUNT TO PAY:{}".format(totamt))
print("="*50)