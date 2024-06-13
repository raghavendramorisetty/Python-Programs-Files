#Program for Executing Functions by Mutiple Sub Threads and Main Thread
#ProgramaticPythonExecEnv.py
import threading
def hello():
	print("hello() executed by:",threading.current_thread().name)
def hi():
	print("hi() executed by:",threading.current_thread().name)
def greet():
	print("greet() executed by:",threading.current_thread().name)

#Main Program
print("*"*50)
print("Program Execution started by:",threading.current_thread().name)
print("*"*50)
#Create Sub Threads for excuting 3 sub Threads
t1=threading.Thread(target=hello)
t1.name="Lohit"
t2=threading.Thread(target=hi)
t2.name="Mayank"
t3=threading.Thread(target=greet)
t3.name="Rakesh"
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("*"*50)
print("Program Execution ended by:",threading.current_thread().name)
print("*"*50)