# Program for Reading the Values from KBD by using Comprehension Concept
# SetComprHenEx1.py
print("Enter Number of Values separated by space:")
st1 = {int(val) for val in input().split()}
print("content of set=", st1)
