#program for Reading the Data from CSV File in the form of Dict--book.csv
#CSVReaderEx4.py
import csv
try:
    fp=open("book1.csv","r")
except FileNotFoundError:
    print("CSV File does not exist")
else:
    csvdr=csv.DictReader(fp) #here csvdr is an object of type < class, csv.DictReader>
    for record in csvdr:
        for key,value in record.items():
            print("\t{}--->{}".format(key,value))
        print()
        print("-"*50)
