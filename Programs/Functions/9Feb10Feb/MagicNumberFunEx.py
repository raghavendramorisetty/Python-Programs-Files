#MagicNumberFunEx.py
def magicnumber():
    n=int(input("Enter a Number:"))
    res=n**2
    sn=str(n)
    sres=str(res)
    if(sn==sres[-len(sn):]):
        return("{} Is a Magic Number".format(sn))
    else:
        return("{} Is Not a Magic Number".format(sn))

#Main Program
res=magicnumber() # Function Call
print(res)