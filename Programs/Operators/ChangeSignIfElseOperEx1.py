#Program for Changing the sign of the given number
#ChangeSignEx1.py
n=float(input("Enter a Number:")) # 0
cn=-1*n
print("Given Number={}\t\t\tChanged Sign Number={}".format(n,cn))
print("*"*50)
res=-1*n  if n>0 else -1*n if n<0 else "  is Zero Only-no sign changing"
print("{} is {}".format(n,res))