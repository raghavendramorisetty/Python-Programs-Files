#program for demonstrating globals()
#globalsFunEx3.py
a=10
b=20
c=30
d=40 # Here  a,.b,c,d are called global variables
def   operation():
	a=100
	b=200
	c=300
	d=400  # Here a,b,c,d are called Local Variables but have similar names as global variables
	res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
	print("Sum=",res)

#Main Program
operation()
