#Others5.py--Don't try to execute this program bcoz Class Name encapsulated
from Account5 import Account # Gives ImportError Bcoz Class Name made as Encapsulated
ac=Account() # Object Creation
print("-------------------------------------")
print("Account Number:{}".format(ac.acno))
print("Account Holder Name:{}".format(ac.cname))
print("Account Balance:{}".format(ac.bal))
print("Account PIN:{}".format(ac.pin))
print("Account Branch Name:{}".format(ac.bname))
print("-------------------------------------")