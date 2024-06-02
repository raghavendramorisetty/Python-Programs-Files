#ReduceEx3.py
import functools as ft
print("Enter List of Words Separated by Comma for Getting line of text :")
lst=[val for val in input().split(",")] # lst=["Python","is","an","OOP","Lang"]
#get line of text
line=ft.reduce(lambda k,v : k+" "+v , lst)
print("Line of Text={}".format(line))