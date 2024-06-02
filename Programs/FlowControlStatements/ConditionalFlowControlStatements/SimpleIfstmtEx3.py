#Program for accepting the digit  and display its name
#SimpleIfStmtEx3.py
d=int(input("Enter a Digit:")) # d=0  1   2   3   4   5   6   7   8   9
if(d==0):
    print("{} is ZERO".format(d))
if(d==1):
    print("{} is ONE".format(d))
if(d==2):
    print("{} is TWO".format(d))
if(d==3):
    print("{} is THREE".format(d))
if(d==4):
    print("{} is FOUR".format(d))
if(d==5):
    print("{} is FIVE".format(d))
if(d==6):
    print("{} is SIX".format(d))
if(d==7):
    print("{} is SEVEN".format(d))
if(d==8):
    print("{} is EIGHT".format(d))
if(d==9):
    print("{} is NINE".format(d))
if( d  in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is -VE DIGIT".format(d))
if( d not in [0,1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is not a single Digit, but its a Number".format(d))