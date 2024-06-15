# Program for Client Replies Based on Server Message
# ClientChat.py
import socket

while (True):
    cs = socket.socket()
    cs.connect(("127.0.0.1", 9999))
    cdata = input("Student-->")
    if (cdata.lower() == "bye"):
        cs.send(cdata.encode())
        break
    else:
        cs.send(cdata.encode())
        sdata = cs.recv(1024).decode()
        print("KVR-->", sdata)
