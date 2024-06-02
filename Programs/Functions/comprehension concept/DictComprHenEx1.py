#Program for Reading the Words from KBD  and find the words length by using Comprehension Concept
#DictComprHenEx1.py
print("Enter Number of Words separated by Comma:")
d= { word:len(word) for word in input().split(",") }
print(d)

