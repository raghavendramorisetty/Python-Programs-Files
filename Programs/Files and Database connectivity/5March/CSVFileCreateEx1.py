# Program for Creating CSV File by using Python CSV Module--list in list
# CSVFileCreateEx1.py
import csv  # step-1

with open("book1.csv", "a") as fp:  # step-2
    hnames = ["BNO", "NAME", "PRICE"]  # step-3
    recs = [[100, "python", 567.89],
            [101, "Django", 167.89],
            [102, "data sci", 367.12],
            [103, "R", 267.75]] # Records are organised in the form of list in list--step-4
    # create an object of csv writer
    csvwr = csv.writer(fp)
    print(csvwr)#here csvwr is object <class, _csv.writer>
    #write header names to the csv file--use writerow() present in csv.writer class object -- step--6
    csvwr.writerow(hnames)
    # write records to csv file -- use writerows() present in csv.writer class object step-7
    csvwr.writerows(recs)
    print("csv file created --verify")