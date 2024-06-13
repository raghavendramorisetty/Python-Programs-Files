# Program for demonstrating sub threads and start()
# OOPSubThreadEx3.py
import threading


class Hyd:
    def hello(self, val):
        print("{}--->Good Evening:{}".format(threading.current_thread().name, val))


class Bang:
    def hi(self):
        print("{}--->Read Notes well".format(threading.current_thread().name))


# Main Program
print("Prog Execution Started:{}".format(threading.current_thread().name))
# Create Sub Thread1 for executing hello()
t1 = threading.Thread(target=Hyd().hello, args=("RS",))  # Here t1 is object-Sub thread whose default name is Thread-1
# Create Sub Thread1 for executing hi()
t2 = threading.Thread(target=Bang().hi)  # Here t2 is object-Sub thread whose default name is Thread-2
# Dispatch the sub threads t1 and t2 by using start
t1.start()
t2.start()
