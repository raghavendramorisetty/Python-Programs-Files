#icici.py---File Name and acts as Module Name
bname="ICICI"
addr="AMPT--HYD"  # Here bname, addr are called Global Variables
def  simpleint():  # Function Definition
    p=float(input("Enter Principle Amount:"))
    t=float(input("Enter Time:"))
    r=float(input("Enter Rate of Interrest:"))
    #Cal si and totamt to pay
    si=(p*t*r)/100
    totamt=p+si
    print("*"*50)
    print("\t\tSimple Interest result")
    print("*" * 50)
    print("\t\tPrinciple Amount:{}".format(p))
    print("\t\tTime:{}".format(t))
    print("\t\tRate of Interrest:{}".format(r))
    print("\t\tSimple Interest:{}".format(si))
    print("\t\tTOTAL AMOUNT:{}".format(totamt))
    print("*" * 50)