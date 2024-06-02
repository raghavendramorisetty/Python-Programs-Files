#programfor Reading emp record  employee File by using un-pickling process
#EmpUnPickEx2.py
import pickle
def reademprecord():
    try:
        with open("emp.data","rb") as fp:
            print("------------------------------------------------")
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("----------------------------------------")
                    break
    except FileNotFoundError:
        print("File Does not Exist")

# Main program
reademprecord() # Function call
