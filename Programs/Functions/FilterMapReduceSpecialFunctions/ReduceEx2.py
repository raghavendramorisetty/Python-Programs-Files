# ReduceEx2.py
import functools as ft

print("Enter List of Values Separated by space for finding Max and Min:")
lst = [int(val) for val in input().split()]  # lst=[10,3,14,15,5,16,-2,16]
maxv = ft.reduce(lambda a, b: a if a > b else b, lst)
minv = ft.reduce(lambda a, b: a if a < b else b, lst)
print("Max({})={}".format(lst, maxv))
print("Min({})={}".format(lst, minv))
