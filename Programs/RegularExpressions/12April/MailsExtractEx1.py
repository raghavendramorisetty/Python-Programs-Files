#Program for extracting Mails from File
#MailsExtractEx1.py
import re
try:
	with open("mails.info","r") as fp:
		filedata=fp.read()
		print("--------------------------------")
		print("Mails")
		print("--------------------------------")
		mailslist=re.findall(r"\S+@\S+",filedata)
		#print(mailslist)
		for mail in mailslist:
			print(mail)
		print("--------------------------------")
except FileNotFoundError:
	print("File does not exist")

