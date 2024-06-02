#program for cal are and circumfrence of Circle
#CircleAreaCir.py
r=float(input("Enter Radius:"))
ac=3.14*r*r
pc=2*3.14*r
print("="*40)
print("\tRadius={}".format(r))
print("Area of Circle={}".format(ac))
print("Circumfrence of Circle={}".format(pc))
print("="*40)
print("+==========OR==================")
print("\tRadius={}".format(r))
print("Area of Circle={}".format(round(ac,2)))
print("Circumfrence of Circle={}".format(round(pc,2)))
print("="*40)
print("+==========OR==================")
print("\tRadius= %0.2f" %r)
print("Area of Circle= %0.2f" %ac)
print("Circumfrence of Circle= %0.2f" %pc)