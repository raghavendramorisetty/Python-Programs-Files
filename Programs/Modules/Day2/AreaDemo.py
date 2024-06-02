# AreaDemo.py---File Name and Main Program
from menu import menu
import sys
from Rect import area as ra
from Square import area as sa
from Circle import area as ca
from Triangle import area as ta
while(True):
	menu()
	ch=int(input("Enter Ur Choice:"))
	match(ch):
		case 1: ra()
		case 2: sa()
		case 3: ca()
		case 4: ta()
		case 5:
			print("Thx for using this program")
			sys.exit()
		case _:
			print("Ur Selection of Operation is wrong-try again")
