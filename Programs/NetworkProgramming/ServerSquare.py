#Server Program accepting a Numerical value from Client side program and gives Its Square to Client Side Program
#ServerSquare.py
import socket  # Step-1
#Step-2
s=socket.socket()
s.bind(("localhost",8888))
s.listen(1)
print("Server Side Program is Ready to accept any Client Side program request")
while(True):
	try:
		cs,ca=s.accept()  # Step-3
		#Step-4
		cdata=cs.recv(1024).decode()
		print("Client Data at Server Side=",cdata)
		csval=float(cdata)
		res=csval**2
		#Step-5
		cs.send(str(res).encode())
	except ValueError:
		cs.send("Don't enter alnums,strs and symbols-plz enter Numerical Val".encode())