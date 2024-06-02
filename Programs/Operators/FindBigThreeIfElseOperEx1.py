#Program for Finding Bigegst Three Numbers and Check for Equality
#FindBigThreeEx1.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=float(input("Enter Third Value:"))
#Logic for Biggest of three
big=a if a>=b and a>c else b if b>=c and b>a else c if c>=a and c>b else "All are equal"
print("Big({},{},{})={}".format(a,b,c,big))