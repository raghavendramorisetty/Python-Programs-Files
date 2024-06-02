#Program for Demonstrating How to write Iterable Object data to the file
#FileWriteEx3.py
x={10:"Python",20:"Java",30:"C",40:"HTML","Talent":None}  # Here x is an Iterable object
with open("sci.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data written to the File")
