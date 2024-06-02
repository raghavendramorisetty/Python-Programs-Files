#MatchCaseEx5.py
wkd=input("Enter week Name:")
if wkd.lower() in ("monday","tuesday","wednesday","thursday","friday","sunday","saturday","mon","tue","wed","thu","fri","sat","sun"):
	match(wkd.lower()[0:3]):
		case "mon"|"tue"|"wed"|"thu"|"fri":
			print("{} is Working Day:".format(wkd))
		case "sat":
			print("{} is Week-End:".format(wkd))
		case "sun":
			print("{} is holi Day:".format(wkd))
else:
	print("{} is not a week Day".format(wkd))
