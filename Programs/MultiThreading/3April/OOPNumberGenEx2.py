# Program for generating 1 to n numbers by using threads--Object oriented Programming
# OOPNumberGenEx1.py
import threading, time


class Numbers:
    def __init__(self, n):
        self.n = n

    def generate(self):
        if (self.n <= 0):
            print("{}--->{} is Invalid Input".format(threading.current_thread().name, n))
        else:
            print("-------------------------------------------------------")
            print("Numbers within :{}".format(self.n))
            print("-------------------------------------------------------")
            for i in range(1, self.n + 1):
                print("{}--->Value of i={}".format(threading.current_thread().name, i))
                time.sleep(0.25)
            print("-------------------------------------------------------")


# Main Program
# Create sub thread for executing generate()
n = int(input("Enter How Many Numbers u want to Generate:"))
no = Numbers(n)  # Object Creation--calls Constructor
t1 = threading.Thread(target=no.generate)
t1.name = "KVR"
t1.start()
