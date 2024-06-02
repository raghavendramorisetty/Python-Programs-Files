#Program for Obtaining the connection from Oracle Database
#OracleConnTestEx2.py
import oracledb as orc # Step-1
try:
    orc.init_oracle_client()
    con=orc.connect("system/manager@127.0.0.1/xe") # Step-2
    print("Python Program Got Connection from Oracle Database")
except orc.DatabaseError as db:
    print("Problem in Oracle Database: ", db)