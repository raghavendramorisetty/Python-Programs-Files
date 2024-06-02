#program for Reading emp record  employee File by using un-pickling process
#EmpUnPickEx1.py
import pickle
try:
    with open("emp.data","rb") as fp:
        print("-----------------------------------------------")
        while(True):
            try:
                record = pickle.load(fp) # Raises EOFError if file reaches End
                #print(record,type(record))
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("---------------------------------------")
                break
except FileNotFoundError:
    print("File does not Exist")

