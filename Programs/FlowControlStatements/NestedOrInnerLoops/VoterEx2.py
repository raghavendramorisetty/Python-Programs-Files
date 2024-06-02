#VoterEx1.py
while(True):
        age=int(input("Enter Age of Citizen:"))
        if(age>=18) and (age<=100):  #OR  (18<=age<=100)
            print("{} Years Citizen is Eligible to Vote:".format(age))
            break
        else:
            print("\t{} Years Citizen is not Eligible to Vote: try again".format(age))