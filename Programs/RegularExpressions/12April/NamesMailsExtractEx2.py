#Program for extracting Names and Mails from File
#NamesMailsExtractEx2.py
import re
try:
	with open("mails.info","r") as fp:
		filedata=fp.read()
		mailslist=re.findall(r"\S+@\S+",filedata)
		nameslist=re.findall("[A-Z][a-z]+",filedata) # Must have capitals and small-letters in the names of mails.info file
		print("-----------------------------------------")
		print("Names\tMails")
		print("-----------------------------------------")
		for names,mails in zip(nameslist,mailslist):
			print("{}\t{}".format(names,mails))
		print("-----------------------------------------")
	
except FileNotFoundError:
	print("File does not exist")