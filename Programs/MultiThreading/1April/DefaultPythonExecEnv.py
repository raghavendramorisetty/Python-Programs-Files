#Program for Executing Functions by Single Thread
#DefaultPythonExecEnv.py
import threading
def hello():
	print("hello() executed by:",threading.current_thread().name)
def hi():
	print("hi() executed by:",threading.current_thread().name)
def greet():
	print("greet() executed by:",threading.current_thread().name)

#Main Program
print("Program Execution started by:",threading.current_thread().name)
hello()
hi()
greet()
print("Program Execution ended by:",threading.current_thread().name)
