h=float(input("Enter height of triangle:"))
b=float(input("Enter Breadth of triangle:"))
area=(0.5*b*h)
print("#"*45)
print("\t\tarea of triangle={}".format(area))
print("#"*45)
print("+==========(OR) Using Other Formula==================")
print("Enter the three sides of triangle")
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
area2=(s*(s-a)*(s-b)*(s-c))**0.5
print("#"*70)
print("\t\tarea of triangle using formula 2 = {}".format(area2))
print("#"*70)




