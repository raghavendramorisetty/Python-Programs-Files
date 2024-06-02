#SharesDemo.py
import Shares,time,importlib
def disp(d):
    print("-"*50)
    print("\tShareName\tShareValue")
    print("-" * 50)
    for sn,sv in d.items():
        print("\t{}\t\t\t\t{}".format(sn,sv))
    print("-" * 50)

#Main program
d=Shares.sharesinfo()
disp(d)
print("I am going to sleep for 15 Seconds")
time.sleep(15)
print("I am coming out-of sleep after 15 second")
importlib.reload(Shares)
d=Shares.sharesinfo()
disp(d)
print("I am going to sleep for 15 Seconds")
time.sleep(15)
print("I am coming out-of sleep after 15 second")
importlib.reload(Shares)
d=Shares.sharesinfo()
disp(d)
