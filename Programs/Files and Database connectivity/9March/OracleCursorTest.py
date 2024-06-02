#Program for creating Cursor object
#OracleCursorTest.py
import oracledb as orc # step-1
orc.init_oracle_client()
con=orc.connect("system/manager@localhost/xe") #step-2
print("Type of con=",type(con)) # <class 'oracledb.Connection'>
print("Python Program Got Connection from Oracle Database")
print("----------------------------------------------------------------------")
cur=con.cursor() #step-3
print("Type of cur=",type(cur)) # <class 'oracledb.Cursor'>
print("Python Program created a cursor object")
print("----------------------------------------------------------------------")
