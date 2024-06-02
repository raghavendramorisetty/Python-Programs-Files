#FiguresArea.py----File Name and Module name
def rarea():
	print("Enter Length and Breadth:")
	l,b=float(input()),float(input())
	print("Area of Rect={}".format(l*b))
def sarea():
	s=float(input("Enter Side:"))
	print("Area of Square={}".format(s**2))
def carea():
	r=float(input("Enter Radius of Circle:"))
	print("Area of Circle={}".format(3.14*r**2))
def tarea():
	print("Enter Base and Height of Triangle:")
	b,h=float(input()),float(input())
	print("Area of Triangle={}".format((1/2)*b*h))