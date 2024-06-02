#Program for accepting the digit  and display its name
#DigitEx.py
d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
digit=int(input("Enter a Digit:")) # d=0  1   2   3   4   5   6   7   8   9
res=d.get(digit) if d.get(digit)!=None\
    else "-VE Digit" if digit in [-1,-2,-3,-4,-5,-6,-7,-8,-9] \
    else "+VE Number" if digit >0 and digit not in [0,1,2,3,4,5,6,7,8,9] \
    else " -VE NUMBER"
print("{} is {}".format(digit,res))