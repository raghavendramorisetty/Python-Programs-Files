#Program for Demonstrating generators
#GenEx5.py
import sys
def getcrses():
	yield "PYTHON"
	yield "Django"
	yield "Data Science"
	yield "ML"

#Main program
g=getcrses()
print(next(g))
print(next(g))
print(next(g))