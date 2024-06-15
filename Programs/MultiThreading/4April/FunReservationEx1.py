# Program for Reservation of Seats
# FunReservationEx1.py
import threading, time

def seatreserve(seats):
    K.acquire()
    global nos
    if (seats > nos):
        print("-------------------------------------------------")
        print("Hi '{}' ,{} Seats are Not Available-Try latter".format(threading.current_thread().name, seats))
        time.sleep(2)
    else:
        print("-------------------------------------------------")
        nos = nos - seats
        print("Hi '{}' ,{} Seats are Reserved--Hpy Journey".format(threading.current_thread().name, seats))
        time.sleep(2)
        print("Number of Available Seats:{}".format(nos))
        time.sleep(2)
        if (nos == 0):
            print("Train is Full")
    print("-------------------------------------------------")
    K.release()


# Main Program
K = threading.Lock()
nos = 15
t1 = threading.Thread(target=seatreserve, args=(8,))
t1.name = "RS"
t2 = threading.Thread(target=seatreserve, args=(9,))
t2.name = "TR"
t3 = threading.Thread(target=seatreserve, args=(5,))
t3.name = "MC"
t4 = threading.Thread(target=seatreserve, args=(3,))
t4.name = "DR"
t5 = threading.Thread(target=seatreserve, args=(1,))
t5.name = "GS"
t6 = threading.Thread(target=seatreserve, args=(1,))
t6.name = "DS"
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
