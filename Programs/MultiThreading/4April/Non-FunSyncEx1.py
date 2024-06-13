#Program for Demonstarting Dead Lock Occurance
#Non-FunSyncEx1.py
import threading,time
def  multable(n):
	if(n<=0):
		print("{} -->{} Invalid input".format(threading.current_thread().name,n))
	else:
		print("Mul table for {}".format(n))
		print("------------------------------------------------")
		for i in range(1,11):
			print("{}-->{} x {}={}".format(threading.current_thread().name,n,i,n*i))
			time.sleep(1)
		else:
			print("------------------------------------------------")
#Main Program
t1=threading.Thread(target=multable,args=(10,))
t2=threading.Thread(target=multable,args=(19,))
t3=threading.Thread(target=multable,args=(14,))
t4=threading.Thread(target=multable,args=(9,))
#dispatch the therads
t1.start()
t2.start()
t3.start()
t4.start()
