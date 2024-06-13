#Program for demonstrating setting and getting the name of threads
#SetGetThreadNames.py
import threading
def  hello(val):
	print("{}--->Good Evening:{}".format(threading.current_thread().name,val))

def  hi():
	print("{}--->Read Notes well".format(threading.current_thread().name))

#Main Program
print("Prog Execution Started:{}".format(threading.current_thread().name))
#Create Sub Thread1 for executing hello()
t1=threading.Thread(target=hello,args=("RS",) ) # Here t1 is object-Sub thread whose default name is Thread-1
#Create Sub Thread1 for executing hi()
t2=threading.Thread(target=hi)# Here t2 is object-Sub thread whose default name is Thread-2
#Get the Name of the sub threads
#print("Name of First Sub Thread=",t1.getName()) Here getName() is Deprecated on the name of "name" attribute
print("Name of First Sub Thread=",t1.name) # Thread-1 (hello)
print("Name of Second Sub Thread=",t2.name) #Thread-2 (hi)
print("Name of the Main Thread=",threading.current_thread().name) # Main Thread
print("----------------------------------------------------------------------")
#Set the User-Friendly Name to the Sub Threads
#t1.setName("Greet")---Here getName() is Deprecated on the name of "name" attribute
t1.name="Greet"
t2.name="advise"
print("Name of First Sub Thread after setting=",t1.name) # greet
print("Name of Second Sub Thread after setting=",t2.name) # advise
print("*"*50)
t1.start()
t2.start()
t1.join()
t2.join()