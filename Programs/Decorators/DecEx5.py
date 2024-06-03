#Program for accepting Line of Text and Obtaining each word name in upper case  and its length by using decorator
#DecEx5.py
def wordcount(linespl):
	def countvalues():
		line,words=linespl()
		d={} # Create empty Dict
		for word in words:
			d[word.upper()]=len(word)
		return line,words,d
	return countvalues

def linesplit(getline):
	def separate():
		line=getline()
		words=line.split()
		return line,words
	return separate

@wordcount
@linesplit
def  getline():
	return(input("Enter a Line of Text:"))

#Main Program
hyd=getline() # Normal Function Call
#Here hyd is the tuple.
print("Given Line={}".format(hyd[0]))
print("Given Words={}".format(hyd[1]))
print("Words Count={}".format(hyd[2]))