#Program for Demonstrating global Keyword
#GlobalKwdEx2.py
a=10 # Here 'a' is called Global variable
b=20 # Here 'b' is called Global variable
def  incr1():
	global a,b # Mandatory to write global Kwd bcoz we are modifying the global var value a and b
	a=a+1
	b=b+1
def incr2():
	global a,b # Mandatory to write global Kwd bcoz we are modifying the global var value a and b
	a=a*2
	b=b*2
def  incr3():
	c=a*3  # Here we need not to use global keyword bcoz we are not modifying global var value 'a'
	d=b*3  # Here we need not to use global keyword bcoz we are not modifying global var value 'a'
#Main program
print("a= {} b={} in Main Program before incr1()".format(a,b)) # a=10  b=20
incr1()
print("a= {} b={} in Main Program after incr1()".format(a,b)) # a=11  b=21
incr2()
print("a= {} b={} in Main Program after incr2()".format(a,b)) # a=22 b=42
incr3()
print("a= {} b={} in Main Program after incr3()".format(a,b)) # a=22 b=42