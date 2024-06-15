#Program for Demonstrating generators
#GenEx2.py
import sys
def  kvrgen(x):
	i=0
	while(i<x):
		yield i
		i=i+1

#Main program
r=kvrgen(6) # here r is an object of <class, 'generator'>
while(True):
	try:
		print(next(r))
	except StopIteration:
		break
