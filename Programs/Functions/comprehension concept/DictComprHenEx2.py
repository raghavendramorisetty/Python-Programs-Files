#Program for accepting List of Words and Obtain words along with upper case words by using Dict Comprehesion concept
#DictComprHenEx2.py
print("Enter List of words separated by comma:")
words={word:word.upper() for word in input().split(",")}
print(words)
