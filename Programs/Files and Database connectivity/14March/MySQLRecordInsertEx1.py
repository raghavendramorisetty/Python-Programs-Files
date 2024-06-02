#Program for Inserting employee values as Record in employee table
#MySQLRecordInsertEx1.py
import mysql.connector

#Development of Programmer-Defined Exceptions
class InvalidNameError(Exception):pass
class SpaceError(BaseException):pass
#Define a Function for Validating Employee Name and comp name
def  validation(name):
    words=name.split()
    if(len(words)==0):
        raise SpaceError
    else:
        x="Valid"
        for word in words:
            if(not word.isalpha()):
                x="Invalid"
                break
        if(x=="Invalid"):
            raise InvalidNameError
        else:
            return name

def  recordinsert():
    while(True):
        try:
            con = mysql.connector.connect(host="127.0.0.1",
                                          user="root",
                                          passwd="root",
                                          database="6pmbatch")

            cur=con.cursor()
            #Accept Employee Values from Key Board
            print("*"*50)
            empno=int(input("Enter Employee Number:"))
            ename=validation(input("Enter Employee Name:"))
            empsal=float(input("Enter Employee Salary:"))
            compname=validation(input("Enter Employee Company Name:"))
            print("*" * 50)
            #design the query and execute
            iq="insert into employee values(%d,'%s' ,%f,'%s') "
            cur.execute(iq %(empno,ename,empsal,compname))
            #OR
            #cur.execute("insert into employee values(%d,'%s' ,%f,'%s') "%(empno,ename,empsal,compname))
            con.commit()
            #print("%d Record Inserted in Employee Table--verify " %cur.rowcount)  OR
            print("{} Record Inserted in Employee Table--verify " .format(cur.rowcount))
            print("*" * 50)
            ch=input("Do u want to Insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for this Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB: ",db)
        except ValueError:
            print("Don't enter Alnums,strs and symbols for empno and salary:")
        except InvalidNameError:
            print("Employee Name OR Comp Name Must Have Only Alphabets-But not Non-alphas ")
        except SpaceError:
            print("Employee Name OR Comp Name Should't be Empty")
        except:
            print("Ooooops Some thing went wrong--try again")
#main program
recordinsert() # Function call