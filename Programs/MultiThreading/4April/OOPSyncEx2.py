# Program for Demonstrating by eliminating Dead Lock
# OOPSyncEx2.py
import threading, time


class Table:
    @classmethod
    def getlock(cls):
        cls.K = threading.Lock()  # Here K is called Class Level Var--Treated as Lock object

    def multable(self, n):
        # Get the lock
        self.K.acquire()
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
        self.K.release()


# Main Program
Table.getlock()
t1 = threading.Thread(target=Table().multable, args=(10,))
t2 = threading.Thread(target=Table().multable, args=(-19,))
t3 = threading.Thread(target=Table().multable, args=(14,))
t4 = threading.Thread(target=Table().multable, args=(-9,))
# dispatch the therads
t1.start()
t2.start()
t3.start()
t4.start()