#program for demonstrating globals()
#globalsFunEx1.py
a=10
b=20
c=30
d=40 # Here a,b,c,d are called global variables
def   operation():
	a=100
	b=200
	c=300
	d=400  # Here a,b,c,d are called Local Variables but have similar names as global variables
	d=globals()
	print("Global Variables of Current Program and Invisiblle Global Variable")
	print("Number of GV=",len(d))
	for gvn,gvv in d.items():
		print("\t{}--->{}".format(gvn,gvv))
	print("------------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--way-1")
	print("------------------------------------------------------------------------------")
	print("Global Var a=",d['a'])
	print("Global Var b=",d['b'])
	print("Global Var c=",d['c'])
	print("Global Var d=",d['d'])
	print("------------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--way-2")
	print("------------------------------------------------------------------------------")
	print("Global Var a=",d.get('a'))
	print("Global Var b=",d.get('b'))
	print("Global Var c=",d.get('c'))
	print("Global Var d=",d.get('d'))
	print("------------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--way-3")
	print("------------------------------------------------------------------------------")
	print("Global Var a=",globals().get('a'))
	print("Global Var b=",globals().get('b'))
	print("Global Var c=",globals().get('c'))
	print("Global Var d=",globals().get('d'))
	print("------------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--way-4")
	print("------------------------------------------------------------------------------")
	print("Global Var a=",globals()['a'])
	print("Global Var b=",globals()['b'])
	print("Global Var c=",globals()['c'])
	print("Global Var d=",globals()['d'])
	print("------------------------------------------------------------------------------")

#Main Program
operation()
