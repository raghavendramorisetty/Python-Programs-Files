#Program for demonstrating joining the sub threads
#JoiningThreads.py
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
st1.name="ChildThread"
#dispatch the sub thread
st1.start()
print()
print("Number of Active Threads after dispatch=",threading.active_count())
st1.join()
print("Number of Active Threads after join=",threading.active_count())
print("Program Execution Ended:{}".format(threading.current_thread().name))