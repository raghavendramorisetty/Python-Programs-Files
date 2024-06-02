#program for Reading the Data from CSV File in the form of Dict--employee1.csv
#CSVReaderEx2.py
import csv
try:
    fp=open("employee.csv","r")
except FileNotFoundError:
    print("Csv file does not exist")
else:
    csvdr=csv.DictReader(fp) #here csdr is an object of type <class, csv.DictReader>
    for record in csvdr:
        for key,value in record.items():
            print("\t{}---->{}".format(key,value))
        print("-"*50)