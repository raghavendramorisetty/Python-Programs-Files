#MatchCaseEx3.py
wkd=input("Enter week Name:")
match(wkd):
	case "monday":
		print("{} is Working Day:".format(wkd))
	case "tuesday":
		print("{} is Working Day:".format(wkd))
	case "wednesday":
		print("{} is Working Day:".format(wkd))
	case "thursday":
		print("{} is Working Day:".format(wkd))
	case "friday":
		print("{} is Working Day:".format(wkd))
	case "saturday":
		print("{} is Week -End:".format(wkd))
	case "sunday":
		print("{} is holi Day:".format(wkd))
	case _:
		print("{} is not a week day".format(wkd))