#MatchCaseEx4.py
wkd=input("Enter week Name:")
match(wkd.lower()):
	case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
		print("{} is Working Day:".format(wkd))
	case "saturday":
		print("{} is Week -End:".format(wkd))
	case "sunday":
		print("{} is holi Day:".format(wkd))
	case _:
		print("{} is not a week day".format(wkd))
