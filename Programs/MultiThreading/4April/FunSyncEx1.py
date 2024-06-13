# Program for Demonstarting by eliminating Dead Lock
# FunSyncEx1.py
import threading, time


def multable(n):
    # Get the lock
    L.acquire()
    if (n <= 0):
        print("{} -->{} Invalid input".format(threading.current_thread().name, n))
    else:
        print("Mul table for {}".format(n))
        print("------------------------------------------------")
        for i in range(1, 11):
            print("{}-->{} x {}={}".format(threading.current_thread().name, n, i, n * i))
            time.sleep(0.12)
        else:
            print("------------------------------------------------")
    # Un-lock the object
    L.release()


# Main Program
# Create an object of Lock Class of Threading Module
L = threading.Lock()
t1 = threading.Thread(target=multable, args=(10,))
t2 = threading.Thread(target=multable, args=(-19,))
t3 = threading.Thread(target=multable, args=(14,))
t4 = threading.Thread(target=multable, args=(-9,))
# dispatch the threads
t1.start()
t2.start()
t3.start()
t4.start()