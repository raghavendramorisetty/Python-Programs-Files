import gc
print("Is GC Running?:",gc.isenabled())
print("Program Execution started")
a=10
b=20
c=a+b
gc.disable()
print("Val of a=",a)
print("Val of b=",b)
print("Now Is GC Running?:",gc.isenabled())
print("sum=",c)
gc.enable()
print("Now Is GC Running?:",gc.isenabled())
print("Program execution Ended")