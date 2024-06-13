#Execution time of default thread --MainTherad
#ExecutionTimeWithOutThreads.py
import threading,time
def  squares(lst):
	for val in lst:
		print("{}--->Square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)
def  cubes(lst):
	for val in lst:
		print("{}--->cube({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#Main program
bt=time.time()
print("Program Execution started by:",threading.current_thread().name)
lst=[12,3,4,19,3,15,16,-5]
squares(lst)
cubes(lst)
print("Program Execution Ended by:",threading.current_thread().name)
et=time.time()
print("Total execution --without Sub Therads--",et-bt)