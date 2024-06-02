#AnonymousFunEx2.py
palindrome=lambda word: "Palindrome" if word==word[::-1] else "Not Palindrome"
#Main Program
word=input("Enter a Word OR Value:")
res=palindrome(word) # Function Call
print("{} is {}".format(word,res))
