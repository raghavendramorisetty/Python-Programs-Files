#Program for Obtaining Number of threading which actively running
#Demonstrating active_thread()
#active_threadsCountEx.py
import threading
noth=threading.active_count()
print("Number of Threads Running=",noth) # Number of Threads Running= 1
print("------------------OR----------------------")
print("Number of Threads Running=",threading.active_count())
