# Program for Server Replies Based on Client Message
# ServerChat.py
import socket

ss = socket.socket()
ss.bind(("127.0.0.1", 9999))
ss.listen(2)
print("SSP is ready to accept CSP Request")
while (True):
    cs, ca = ss.accept()
    cdata = cs.recv(1024).decode()
    print("Student-->{}".format(cdata))
    sdata = input("KVR-->")
    cs.send(sdata.encode())
