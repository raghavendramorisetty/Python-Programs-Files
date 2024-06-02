n=int(input('Enter the number of values to sum or product: '))
s1,s2,s3=0,0,0
p=1
i=1
if(n<=0):
    print("invalid input")
else:
    while(i<=n):
        s1=s1+i
        s2=s2+i**2
        s3=s3+i**3
        p=p*i
        i=i+1
    else:
        print("sum of n natural numbers is: {}".format(s1))
        print("sum of squares of n natural numbers is: {}".format(s2))
        print("sum of cubes of n natural numbers {}".format(s3))
        print("product of n natural numbers is: {}".format(p))