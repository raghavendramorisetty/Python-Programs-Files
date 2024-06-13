# Program for Demonstarting by eliminating Dead Lock
# OOPSyncEx3.py
import threading, time


class Table:
    @classmethod
    def getlock(cls):
        cls.K = threading.Lock()  # Here K is called Class Level Var--Treated as Lock object

    def __init__(self, n):
        self.n = n

    def multable(self):
        # Get the lock
        #Table.K.acquire()
        self.K.acquire()
        if (self.n <= 0):
            print("{} -->{} Invalid input".format(threading.current_thread().name, self.n))
        else:
            print("Mul table for {}".format(self.n))
            print("------------------------------------------------")
            for i in range(1, 11):
                print("{}-->{} x {}={}".format(threading.current_thread().name, self.n, i, self.n * i))
                time.sleep(0.12)
            else:
                print("------------------------------------------------")
        # Un-lock the object
        #Table.K.release()
        self.K.release()


# Main Program
Table.getlock()
t1 = threading.Thread(target=Table(19).multable)
t2 = threading.Thread(target=Table(-9).multable)
t3 = threading.Thread(target=Table(14).multable)
t4 = threading.Thread(target=Table(16).multable)
# dispatch the therads
t1.start()
t2.start()
t3.start()
t4.start()
