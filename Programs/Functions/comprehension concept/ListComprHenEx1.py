#Program for Reading the Values from KBD by using Comprehension Concept
#ListComprHenEx1.py
print("Enter Number of numerical Values separated by space:")
lst=[int(val) for val in input().split()]
print("content of list=",lst)