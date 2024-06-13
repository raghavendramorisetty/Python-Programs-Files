# Program for generating 1 to n numbers by using threads--Object oriented Programming
# OOPNumberGenEx1.py
import threading, time

class Numbers:
    def generate(self, n):
        if (n <= 0):
            print("{}--->{} is Invalid Input".format(threading.current_thread().name, n))
        else:
            print("-------------------------------------------------------")
            print("Numbers within :{}".format(n))
            print("-------------------------------------------------------")
            for i in range(1, n + 1):
                print("{}--->Value of i={}".format(threading.current_thread().name, i))
                time.sleep(0.5)
            print("-------------------------------------------------------")


# Main Program
# Create sub thread for executing generate()
n = int(input("Enter How Many Numbers u want to Generate:"))
t1 = threading.Thread(target=Numbers().generate, args=(n,))
t1.name = "KVR"
t1.start()
