# Program for Reading the Values from KBD by using Comprehension Concept
# TupleComprHenEx1.py
print("Enter Number of Values separated by space:")
x = (int(val) for val in input().split())
print("Type of x=", type(x))  # Type of x= <class 'generator'>
# Convert an object of generator into tuple
tpl = tuple(x)
print("content of tuple=", tpl)

