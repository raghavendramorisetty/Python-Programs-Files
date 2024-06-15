#Prpogram for Demonstrating Iterators
#ItrEx2.py
x=(10,"RS",34.56,True,2+3j)
print(x,type(x))
print("----------------------------------")
itrobj=iter(x)
print(type(itrobj))
while(True):
	try:
		print(next(itrobj))
	except StopIteration:
		break