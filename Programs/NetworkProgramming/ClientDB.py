# ClientDB.py
import socket

s = socket.socket()
s.connect(("localhost", 7777))
sno = input("Enter Student Number:")
s.send(sno.encode())
sdata = s.recv(1024).decode()
print("---------------------------------------------")
print(sdata)
print("---------------------------------------------")
