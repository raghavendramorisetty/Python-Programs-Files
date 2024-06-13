#Program for Showing default Thread
#DefaultThread.py
import threading
tname=threading.current_thread().name
print("Default name of thread=",tname)
print("Number of Threads which are Running by Default=",threading.active_count())
