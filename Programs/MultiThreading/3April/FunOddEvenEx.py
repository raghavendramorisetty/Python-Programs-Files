# Program for generating Odd Numbers and Even Numbers within the reange of n. where n is +ve by using multiple threads
# FunOddEvenEx.py
import threading, time


def odd(n):
    if (n <= 0):
        print("{}--->{} is Invalid Input".format(threading.current_thread().name, n))
    else:
        for i in range(1, n + 1, 2):
            print("{}--->Odd={}".format(threading.current_thread().name, i))
            time.sleep(1)


def even(n):
    if (n <= 0):
        print("{}--->{} is Invalid Input".format(threading.current_thread().name, n))
    else:
        for i in range(2, n + 1, 2):
            print("{}--->Even={}".format(threading.current_thread().name, i))
            time.sleep(1)


# Main program
ot = threading.Thread(target=odd, args=(int(input("Enter till which number you need Odd Numbers:")),))
et = threading.Thread(target=even, args=(int(input("Enter till which Even Numbers u want:")),))
ot.start()
et.start()
