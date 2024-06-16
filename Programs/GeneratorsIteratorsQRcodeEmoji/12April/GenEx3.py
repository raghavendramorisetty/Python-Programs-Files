#Program for Demonstrating generators
#GenEx3.py
import sys
def  kvrgen(x):
	i=0
	while(i<x):
		yield i
		i=i+1

#Main program
r=kvrgen(6) # here r is an object of <class, 'generator'>
#print(r)
for val in r:
	print(val)