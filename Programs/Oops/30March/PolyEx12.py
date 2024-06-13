#Program for cal area of Different figures by using polymorphism
#PolyEx12.py
class Circle:  # Base Class
    def __init__(self,r): # Original Parameterized Constructor
        self.ac=3.14*r**2
        print("Area of Circle:{}".format(self.ac))
class Square: # Base Class
    def __init__(self,s): # Default Constructor
        self.sa=s**2
        print("Area of Square={}".format(self.sa))
        print("=" * 50)
class Rect(Square,Circle):
    def __init__(self,l,b):  # Overridden Constructor
        self.ar=l*b
        print("Area of Rect={}".format(self.ar))
        print("*"*50)
        Circle.__init__(self,float(input("Enter Radius:")))
        print("*" * 50)
        super().__init__(float(input("Enter Side:")))
#Main Program
l = float(input("Enter Length:"))
b=float(input("Enter Breadth:"))
r=Rect(l,b) # Object Creation