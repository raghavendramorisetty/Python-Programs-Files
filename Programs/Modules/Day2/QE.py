#Program for calculating roots of QE
#QE.py
import math,cmath
def quadeqn():
	a=float(input("Enter Value of a:"))
	b=float(input("Enter Value of b:"))
	c=float(input("Enter Value of c:"))
	D=b**2-4*a*c
	if(D==0):
		print("Roots are Real and Equal")
		root1=-(b/(2*a))
		root2=root1
		print("First Root={}".format(root1))
		print("Second Root={}".format(root2))
	elif(D>0):
		print("Roots are Real and Distinct")
		root1= (-b+math.sqrt(D))/(2*a)
		root2= (-b-math.sqrt(D))/(2*a)
		print("First Root={}".format(root1))
		print("Second Root={}".format(root2))
	elif(D<0):
		print("Roots are Imaginary OR Complex")
		root1=(-b+cmath.sqrt(D))/ (2*a)
		root2=(-b-cmath.sqrt(D))/ (2*a)
		print("First Root={}".format(root1))
		print("Second Root={}".format(root2))
