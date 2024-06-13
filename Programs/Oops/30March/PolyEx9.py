#Program for cal area of Different figures by using polymorphism
#PolyEx8.py
class Circle:  # Base Class
    def area(self,r): # Original Method
        self.ac = 3.14 * r ** 2
        print("Area of Circle:{}".format(self.ac))
        #super().area() This Gives AttributeError bcoz object class does not contain area()
class Square: # Base Class
    def area(self,s): # Original Method
        self.sa = s ** 2
        print("Area of Square={}".format(self.sa))
        print("=" * 50)

class Rect(Circle,Square):
    def area(self,l,b):  # Overridden Method
        self.ar = l * b
        print("Area of Rect={}".format(self.ar))
        print("=" * 50)
        Square.area(self,float(input("Enter Side:")))
        print("=" * 50)
        Circle.area(self, float(input("Enter Radius:")))

#Main Program
r=Rect()
l = float(input("Enter Length:"))
b = float(input("Enter Breadth:"))
r.area(l,b)
