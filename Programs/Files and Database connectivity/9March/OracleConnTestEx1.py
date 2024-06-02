#Program for Obtaining the connection from Oracle Database
#OracleConnTestEx1.py
import oracledb as orc # Step-1
try:
    orc.init_oracle_client()
    con=orc.connect("system/manager@localhost/xe") # Step-2
    print("Type of con=",type(con))
    print("Python Program Got Connection from Oracle Database")
except orc.DatabaseError as db:
    print("Problem in Oracle Database: ", db)
