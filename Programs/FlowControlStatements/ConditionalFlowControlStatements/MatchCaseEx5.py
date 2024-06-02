#MatchCaseEx5.py
wkd=input("Enter week Name:")
match(wkd.lower()[0:3]):
	case "mon"|"tue"|"wed"|"thu"|"fri":
		print("{} is Working Day:".format(wkd))
	case "sat":
		print("{} is Week -End:".format(wkd))
	case "sun":
		print("{} is holi Day:".format(wkd))
	case _:
		print("{} is not a week day".format(wkd))
