# ME
def  convertromantonumber():
    R=input("Enter a Roman Number for Converting Eqv Ordinary Number:")
    R=R.upper()
    N=0
    d1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    d2 = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i=0
    while(i<len(R)):
            if (R[i:i+2] in d2):
                N=N+d2[R[i:i+2]]
                i=i+2
            elif (R[i] in d1):
                N=N+d1[R[i]]
                i=i+1
    print(N)

convertromantonumber()

# OR

print("*"*100)

def  convertromantonumber2():
    R=input("Enter a Roman Number for Converting into Eqv Ordinary Number:")
    R=R.upper()
    N=0
    prevval=0
    d1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for value in R:
        val=d1[value]
        if(val>prevval):
            N=N+(val-2*prevval)
        else:
            N = N + val
        prevval=val
    print(N)

convertromantonumber2()

