# ATMOperations.py<----File Name and Module Name
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00 # Global Variable
def  deposit():
	damt=float(input("Enter UR Deposit  amount :")) # Possibility of generating ValueError(pure strs,alnums, symbols)
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("\tUrAccount xxxxx123 Credited with INR:{}".format(damt))
		print("\tNow Current Balance after deposit in ur Account xxxxxx123 INR:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("Enter UR Withdraw  amount :")) # Possibility of generating ValueError(pure strs,alnums, symbols)
	if(wamt<=0):
		raise WithdrawError
	elif((wamt+500)>bal):
		raise InSuffFundError
	else:
		bal=bal-wamt
		print("\tUrAccount xxxxx123 Debited with INR:{}".format(wamt))
		print("\tNow Current Balance  after withdraw in ur Account xxxxxx123 INR:{}".format(bal))

def  balenq():
	print("\tUr Balance in Account xxxxxx123 INR:{}".format(bal))
