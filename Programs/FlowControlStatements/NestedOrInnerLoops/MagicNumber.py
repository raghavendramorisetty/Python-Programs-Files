# ME

num=int(input("Enter number to find whether is it a magic number or not:"))
sqr=num*num
res=False
i=len(str(sqr))-len(str(num))
if(str(num) in str(sqr)[i:]):
    res=True
if(res):
    print("Magic number")
else:
    print("Not Magic number")

# Do pattern Generations Examples Later(me)