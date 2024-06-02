#Program for Deciding whether the Given Number is +Ve or -Ve or Zero
#PosNegZero.py
n=float(input("Enter a Number:")) # n=0
res="POSSITIVE" if n>0 else "NEGATIVE" if n<0 else "ZERO"
print("{} is {}".format(n,res))