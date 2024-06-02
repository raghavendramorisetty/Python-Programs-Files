#Program for Inserting employee values as Record in employee table
#OracleRecordInsertEx3.py
import oracledb as orc

#Development of Programmer-Defined Exceptions
class InvalidNameError(Exception):pass
class SpaceError(BaseException):pass
# Define a Function for validating Employee Name and comp name
def validation(name):
    words=name.split()
    if(len(words)==0):
        raise SpaceError
    else:
        x="valid"
        for word in words:
            if(not word.isalpha()):
                x="Invalid"
                break
        if(x=="Invalid"):
            raise InvalidNameError
        else:
            return name

def recordinsert():
    while(True):
        try:
            orc.init_oracle_client()
            con=orc.connect("system/manager@localhost/xe")
            cur=con.cursor()
            #Accept employee values from key board
            print("*"*50)
            empno=int(input("Enter Employee Number:"))
            ename = validation(input("Enter Employee Name:"))
            empsal = float(input("Enter Employee Salary:"))
            compname = validation(input("Enter Employee Company Name:"))
            print("*"*50)
            #design the query and execute
            iq="insert into employeedb values(%d,'%s', %f,'%s')"
            cur.execute(iq %(empno,ename,empsal,compname))
            con.commit()
            print("%d Record Inserted in empoyee table--verify" %cur.rowcount)
            print("*"*50)
            ch=input("Do you want to insert another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for this program")
                break
        except orc.DatabaseError as db:
            print("problem in oracle db:",db)
        except ValueError:
            print("Dont enter Alnums,strs and symbols for empno and salary:")
        except InvalidNameError:
            print("Employee name or comp name must have only alphabets--but not non-alphas")
        except SpaceError:
            print("Employee Name or comp name shouldn't be empty")
        except:
            print("Oooops something went wrong --- try again")

#main program
recordinsert() #function call




















