#Program for Demonstrating Global Variables
#LocalGlobalVarEx2.py
def   learnAI():
	sub1="AI"
	print("To develop '{}' Based Applications, we must use '{}' Programming Lang".format(sub1,lang))
def   learnML():
	sub2="ML"
	print("To develop '{}' Based Applications, we must use '{}' Programming Lang".format(sub2,lang))
def   learnDL():
	sub3="DL"
	print("To develop '{}' Based Applications, we must use '{}' Programming Lang".format(sub3,lang))

#Main Program
# learnAI() #----we can't access global Variable 'lang'
lang="PYTHON" # Global Variable
learnML()
learnDL()