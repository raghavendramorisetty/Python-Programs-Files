# Program for Matrix example for Reading the Values from KBD by using Comprehension Concept
# ListComprHenEx4.py
rows = int(input("Enter Number of Rows of matrix:"))
cols = int(input("Enter Number of Columns of matrix:"))
print("Enter the Matrix element values")
matrix = [[int(input("Enter the row*col = {}*{} element's value of matrix: ".format(j,i))) for i in range(cols)] for j in range(rows)]
# In above the Inner list comprehension iterates over each element within a Outer list comprehension
print("Above List comprehension output is: ")
print(matrix)
print("Output in Matrix Form is: ")
for rowvals in matrix:
    print(rowvals)
