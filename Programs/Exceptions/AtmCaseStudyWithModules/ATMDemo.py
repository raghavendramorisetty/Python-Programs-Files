#ATMDemo.py<----Main Program
import sys
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError,WithdrawError,InSuffFundError
while(True):
	menu()
	try:
		ch=int(input("Enter Ur Choice:"))
		match(ch):
			case 1:
				try:
					deposit()
				except ValueError:
					print("Don't try to Deposit alnums,strs and symbols-try again")
				except DepositError:
					print("Don't try deposit -ve  and zero amount ")
			case 2:
				try:
					withdraw()
				except WithdrawError:
					print("Don't try Withdraw -ve  and zero amount ")
				except InSuffFundError:
					print("Ur Account does not have Sufficient Funds----Read Python Notes")
				except ValueError:
					print("Don't try to Withdraw alnums,strs and symbols-try again")
			case 3:
				balenq()
			case 4:
				print("Thx for using this program")
				sys.exit()
			case _:
				print("Ur Selection of Operation is wrong--try again")
	except ValueError:
		print("Don't Enter alnums,strs and symbols for Bank Transaction-try again")