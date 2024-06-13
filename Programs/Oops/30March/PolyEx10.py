#Program for cal area of Different figures by using polymorphism
#PolyEx10.py
class Circle:  # Base Class
    def __init__(self): # Original Constructor
        self.r=float(input("Enter radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle:{}".format(self.ac))
class Square(Circle):
    def __init__(self): # Overridden Constructor
        self.s=float(input("Enter Side:"))
        self.sa=self.s**2
        print("Area of Square={}".format(self.sa))
        print("=" * 50)
        super().__init__()
class Rect(Square):
    def __init__(self):  # Overridden Constructor
        self.l = float(input("Enter Length:"))
        self.b=float(input("Enter Breadth:"))
        self.ar=self.l*self.b
        print("Area of Rect={}".format(self.ar))
        print("="*50)
        super().__init__()
#Main Program
r=Rect() # Object Creation
