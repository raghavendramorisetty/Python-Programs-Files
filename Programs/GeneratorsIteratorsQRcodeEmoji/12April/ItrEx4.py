#Prpogram for Demonstrating Iterators
#ItrEx4.py
x={10:"Python",20:"Java",30:"C"}
print(x,type(x))
print("----------------------------------")
itrobj=iter(x)
print(type(itrobj))
while(True):
	try:
		k=next(itrobj)
		print("\t{}-->{}".format(k,x.get(k)))
	except StopIteration:
		break