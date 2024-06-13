#Program for cal area of Different figures by using polymorphism
#PolyEx8.py
class Circle:  # Base Class
    def area(self,r): # Original Method
        self.ac=3.14*r**2
        print("Area of Circle:{}".format(self.ac))
class Square(Circle):
    def area(self,s): # Overridden Method
        self.sa=s**2
        print("Area of Square={}".format(self.sa))
        print("=" * 50)
        super().area(float(input("Enter Radius:")))

class Rect(Square):
    def area(self,l,b):  # Overridden Method
        self.ar=l*b
        print("Area of Rect={}".format(self.ar))
        print("="*50)
        super().area(float(input("Enter Side:")))

#Main Program
r=Rect()
l = float(input("Enter Length:"))
b = float(input("Enter Breadth:"))
r.area(l,b)
