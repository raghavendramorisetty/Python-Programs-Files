#Execution time of Sub threads along MainTherad
#ExecutionTimeWithThreads.py
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
t1=threading.Thread(target=squares, args=(lst,))
t2=threading.Thread(target=cubes, args=(lst,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Program Execution Ended by:",threading.current_thread().name)
et=time.time()
print("Total execution with Sub Therads--",et-bt)