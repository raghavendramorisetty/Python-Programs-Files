# Program for Reservation of Seats
# OOPsReservationEx1.py
import threading, time


class Train:
    @classmethod
    def getTrainInfo(cls):
        cls.K = threading.Lock()
        cls.nos = 15

    def __init__(self, seats):
        self.seats = seats

    def seatreserve(self):
        #Train.K.acquire()
        self.K.acquire()
        if (self.seats > Train.nos):
            print("-------------------------------------------------")
            print("Hi '{}' ,{} Seats are Not Available-Try latter".format(threading.current_thread().name, self.seats))
            time.sleep(2)
        else:
            print("-------------------------------------------------")
            Train.nos = Train.nos - self.seats
            print("Hi '{}' ,{} Seats are Reserved--Hpy Journey".format(threading.current_thread().name, self.seats))
            time.sleep(2)
            print("Number of Available Seats:{}".format(Train.nos))
            time.sleep(2)
            if (Train.nos == 0):
                print("Train is Full")
        print("-------------------------------------------------")
        #Train.K.release()
        self.K.release()


# Main Program
Train.getTrainInfo()
t1 = threading.Thread(target=Train(8).seatreserve)
t1.name = "RS"
t2 = threading.Thread(target=Train(9).seatreserve)
t2.name = "TR"
t3 = threading.Thread(target=Train(5).seatreserve)
t3.name = "MC"
t4 = threading.Thread(target=Train(3).seatreserve)
t4.name = "DR"
t5 = threading.Thread(target=Train(2).seatreserve)
t5.name = "GS"
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
