#program for Reading the Data from KBD and write it to the file
#DynamicWriteEx.py
print("Enter ur data and press @ to stop: ")
with open("hyd.info","at") as fp:
    while(True):
        data=input("Enter the data to be written into file:")
        if(data!="@"):
            fp.write(data+"\n")
        else:
            print("\nData written to the file")
            break


