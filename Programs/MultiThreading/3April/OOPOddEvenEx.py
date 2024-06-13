#Program for generating Odd Numbers and Even Numbers within the reange of n. where n is +ve by using multiple threads
#OOPOddEvenEx.py
import threading,time
class ODD:
	def  odd(self,n):
		if(n<=0):
			print("{}--->{} is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(1,n+1,2):
				print("{}--->Odd={}".format(threading.current_thread().name,i))
				time.sleep(1)
class EVEN:
	def even(self,n):
		if(n<=0):
			print("{}--->{} is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(2,n+1,2):
				print("{}--->Even={}".format(threading.current_thread().name,i))
				time.sleep(1)
#Main program
ot=threading.Thread(target=ODD().odd,args=(int(input("Enter How Many Odd Numbers u want:")),))
et=threading.Thread(target=EVEN().even,args=(int(input("Enter How Many Even Numbers u want:")),))
ot.start()
et.start()