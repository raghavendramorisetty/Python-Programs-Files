#Program for Demonstrating generators
#GenEx4.py
import sys
def  kvrgen(Start,Stop,Step):
	while(Start<=Stop):
		yield Start
		Start=Start+Step

#Main program
r=kvrgen(10,100,10)
while(True):
	try:
		print(next(r))
	except StopIteration:
		break
