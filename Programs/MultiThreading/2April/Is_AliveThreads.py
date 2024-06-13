#Program for demonstrating the execution status of sub threads
#Is_AliveThreads.py
import threading,time
def  operation():
	for i in range(10):
		print("{} Val of i={}".format(threading.current_thread().name,i))
		time.sleep(1)
	print("Sub Thread came out-off operation()")

#Main program
print("Program Execution Strated:{}".format(threading.current_thread().name))
print("Number of Active Threads=",threading.active_count())
#Create a Sub Thread
st1=threading.Thread(target=operation)
print("/n")
print("is sub thread under execution before dispatch:",st1.is_alive())
st1.name="ChildThread"
#dispatch the sub thread
st1.start()
print("is sub thread under execution after dispatch:",st1.is_alive())
print("Number of Active Threads after dispatch=",threading.active_count())
st1.join()
print("is sub thread under execution after join:",st1.is_alive())
print("Number of Active Threads after join=",threading.active_count())
print("Program Execution Ended:{}".format(threading.current_thread().name))