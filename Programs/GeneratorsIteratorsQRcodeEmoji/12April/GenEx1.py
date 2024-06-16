#Program for Demonstrating generators
#GenEx1.py
import sys
def  kvrgen(x):
	i=0
	while(i<x):
		yield i
		i=i+1

#Main program
r=kvrgen(6) # here r is an object of <class, 'generator'>
try:
	print(next(r))
	print(next(r))
	print(next(r))
	print(next(r))
	print(next(r))
	#print(next(r))
except StopIteration:
	sys.exit()