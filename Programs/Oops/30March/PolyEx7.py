#Program for cal area of Different figures by using polymorphism
#PolyEx7.py
class Circle:  # Base Class
    def area(self): # Original Method
        self.r=float(input("Enter radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle:{}".format(self.ac))
        #super().area() This Gives AttributeError bcoz object class does not contain area()
class Square: # Base Class
    def area(self): # Original Method
        self.s=float(input("Enter Side:"))
        self.sa=self.s**2
        print("Area of Square={}".format(self.sa))
class Rect(Circle,Square):
    def area(self):  # Overridden Method
        self.l = float(input("Enter Length:"))
        self.b=float(input("Enter Breadth:"))
        self.ar=self.l*self.b
        print("Area of Rect={}".format(self.ar))
        print("="*50)
        super().area()
        print("=" * 50)
        Square.area(self)
#Main Program
r=Rect()
r.area()
