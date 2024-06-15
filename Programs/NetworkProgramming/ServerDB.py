# ServerDB.py
import socket, oracledb as orc

s = socket.socket()
s.bind(("localhost", 7777))
s.listen(2)
print("SSP Is ready to accept any CSP request")
while (True):
    try:
        cs, ca = s.accept()
        sno = int(cs.recv(1024).decode())
        print("Client data at Server=", sno)
        # Code Communicating Oracle db
        orc.init_oracle_client()
        con = orc.connect("system/manager@localhost/xe")
        cur = con.cursor()
        cur.execute("select * from studentTable where sno=%d" % sno)
        record = cur.fetchone()
        if (record != None):
            s1 = "Student Number:" + str(record[0])
            s2 = "Student Name:{}".format(record[1])
            s3 = "Student Rank:{}".format(record[2])
            ss = s1 + "\n" + s2 + "\n" + s3
            cs.send(ss.encode())
        else:
            cs.send("No Such record Exist-Check Student Number".encode())
    except ValueError:
        cs.send("Don't enter alnums,strs and symbols for student number".encode())
    except orc.DatabaseError as db:
        cs.send(("Prob in Oracle" + str(db)).encode())
