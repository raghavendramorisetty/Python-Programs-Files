#program for demonstrating globals()
#globalsFunEx2.py
a=10
b=20
c=30
d=40 # Here  a,.b,c,d are called global variables
def   operation():
	x=100
	y=200
	z=300
	k=400  # Here x,y,z,k are called Local Variables and have different names to that of global variables
	res=x+y+z+k+a+b+c+d
	print("Sum=",res)

#Main Program
operation()