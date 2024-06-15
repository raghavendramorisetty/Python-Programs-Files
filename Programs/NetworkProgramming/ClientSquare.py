# Client Side Program must read the data from KeyBoard , send to Server Side program and obtains Its Square from Server Side program.
# ClientSquare.py
import socket  # Step-1

# Step-2
s = socket.socket()
s.connect(("localhost", 8888))
print("Client Side Program Obtains connection from Server Side Program")
print("---------------------------------------------------")
# Step-3
val = input("Enter a Number for Finding Its Square:")
s.send(val.encode())
# Step-4
sdata = s.recv(1024).decode()
print("Square({})={}".format(val, sdata))
