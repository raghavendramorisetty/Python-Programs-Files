#Program for Finding smallest Three Numbers and Check for Equality
#FindSmallThreeEx1.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=float(input("Enter Third Value:"))
#Logic for Biggest of three
big=a if b>a<=c else b if a>=b<c else c if a>c<=b else "All are equal"
print("Big({},{},{})={}".format(a,b,c,big))