# Program for accepting List of values and Obtain Only +ve Values by using Comprehesion concept
# ListComprHenEx2.py
print("Enter List of Values separated by space:")
posvals = [int(val) for val in input().split() if int(val) > 0]
print("List of +VE Values=", posvals)
print("----------------------------------------------------")
print("Enter List of Values separated by space:")
posvals = [int(val) for val in input().split() if int(val) < 0]
print("List of -VE Values=", posvals)
