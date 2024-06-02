#PalindromeFun.py
def palindrome():
    val=input("Enter Any Value:")
    if(val==val[::-1]):
        print("{} is Palindrome".format(val))
    else:
        print("{} is Not Palindrome".format(val))


#Main Program
palindrome() # Function Call