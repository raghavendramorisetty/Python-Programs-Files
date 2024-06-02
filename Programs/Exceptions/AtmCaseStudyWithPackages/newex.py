# newex.py
from functools import reduce

print("Enter List of Values separated by space:")
lst1 = [int(val) for val in input().split()]
print("Content of lst1=", lst1)
print("--------------------------------------------------")
print("Enter List of Values separated space:")
sumpos = reduce(lambda x, y: x + y, list(filter(lambda x: x > 0, list(map(float, input().split())))))
print("sum of +ve Elements=", sumpos)
