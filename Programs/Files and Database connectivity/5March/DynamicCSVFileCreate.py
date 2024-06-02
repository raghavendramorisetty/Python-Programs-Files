#DynamicCSVFileCreate.py
import csv
csvfilename=input("Enter Ur CSV File Name:")
noh=int(input("Enter How Many Columns are there in '{}' : ".format(csvfilename)))
if(noh<=0):
    print("{} is Invalid Invalid Input-try again:".format(noh))
else:
    hn=list() # empty list for storing Header Names
    for i in range(1,noh+1):
        hname=input("Enter {} Header Name for {}:".format(i,csvfilename))
        hn.append(hname)
    else:
        print(hn) # ['TID', 'NAME', 'SUB']
        nor=int(input("Enter How Many records u want to enter in {}".format(csvfilename)))
        if(nor<=0):
            print("{} is invalid Input".format(nor))
        else: # nor=3
            records=[] # Outer List
            for i in range(1,nor+1):
                print("Enter {} Record Details:".format(i))
                print("---------------------------------")
                record=[]
                for val in hn:
                    value=input("Enter Value for {}:".format(val))
                    record.append(value)
                else:
                    records.append(record)
            else:
                print(records)
                #Saves records(csv file data) into the csv file name
                with open(csvfilename,"a") as fp:
                    csvwr=csv.writer(fp)
                    csvwr.writerow(hn)
                    csvwr.writerows(records)
                    print("CSV FIle Created Dynamically--verify")