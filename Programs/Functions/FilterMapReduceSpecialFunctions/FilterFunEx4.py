#FilterFunEx4.py
print("Enter List of Words Separated by Comma:")
lst=[val for val in input().split(",")]
pwlist=list(filter( lambda word:word==word[::-1] , lst))
print("Given List of words={}".format(lst))
print("Palindrome List={}".format(pwlist))