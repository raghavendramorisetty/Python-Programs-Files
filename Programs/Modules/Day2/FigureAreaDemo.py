#FigureAreaDemo.py---File Name and Main Program
from menu import menu
import sys
#from FiguresArea import * Not Recommended to use
from FiguresArea import rarea,sarea,carea,tarea
while(True):
	menu()
	ch=int(input("Enter Ur Choice:"))
	match(ch):
		case 1: rarea()
		case 2: sarea()
		case 3: carea()
		case 4: tarea()
		case 5:
			print("Thx for using this program")
			sys.exit()
		case _:
			print("Ur Selection of Operation is wrong-try again")