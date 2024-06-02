# Program for accepting List of Words and Obtain Only  those words whose words length ranges from 3 to 5by using Comprehesion concept
# ListComprHenEx3.py
print("Enter List of words separated by space:")
words = [word for word in input().split() if 3 <= len(word) <= 5]
print("List Words whose length in 3 to 5=", words)
