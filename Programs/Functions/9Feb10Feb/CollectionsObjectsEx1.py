#CollectionsObjectsEx1.py
def dispvalues(obj):
    print("Type of obj=",type(obj))
    for val in obj:
        print("\t{}".format(val))
    print("----------------------------------")
def dispvalues1(obj):
    print("Type of obj=",type(obj))
    for key,val in obj.items():
        print("\t{}--->{}'".format(key,val))
    print("----------------------------------")
#Main Program
s="PYTHON"
dispvalues((s)) # Function Call--disp str values
lst=[10,20,"Python",2+3j,True,34.56]
dispvalues(lst) # Function Call--disp list values
tpl=("Python","Java","HTML",123,3+4j)
dispvalues(tpl) # Function Call---disp tpl values
st={10,20,30,40,50,60,"HYD"}
dispvalues(st) # Function Call ---disp set values
d1={10:"Python",20:"Java",30:"Django",40:"HTML"}
dispvalues1(d1)# Function Call--disp dict values