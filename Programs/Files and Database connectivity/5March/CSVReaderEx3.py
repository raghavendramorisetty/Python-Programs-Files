#program for Reading the Data from CSV File--employee1.csv
#CSVReaderEx3.py
import csv
try:
    with open("book1.csv","r") as fp:
        csvr=csv.reader(fp) # here csvr is an object of <class, _csv.reader>
        print(csvr,type(csvr))
        for record in csvr:
            for val in record:
                print("\t{}".format(val),end="\t")
            print()
except FileNotFoundError:
    print("CSV File Does not exist")


