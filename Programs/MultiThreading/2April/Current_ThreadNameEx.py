#Program for Obtaining Name of Thread which is currently executing
#Demonstrating current_thread()
#Current_ThreadNameEx.py
import threading
t=threading.current_thread()
print(t)  # <_MainThread(MainThread, started 24464)>
print(type(t))
print("-------------------------------------------------------------")
print("Name of the thread=",t.name) # Main Thread
print("----------------------OR---------------------------------------")
print("Name of the thread=",threading.current_thread().name)# Main Thread
print("-------------------------------------------------------------")
