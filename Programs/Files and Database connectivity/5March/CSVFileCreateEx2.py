# Program for Creating CSV File by using Python CSV Module--dict
# CSVFileCreateEx2.py
import csv

with open("grocery1.csv", "a") as fp:
    hname = ["PCODE", "PNAME", "PRICE"]
    records = [{"PCODE": "p100", "PNAME": "colgate", "PRICE": 120},
               {"PCODE": "p120", "PNAME": "Maggi", "PRICE": 160},
               {"PCODE": "p170", "PNAME": "GoodDay", "PRICE": 70},
               {"PCODE": "p180", "PNAME": "RedBull", "PRICE": 140}]
    # To create a csv file by using dict data, we must create an object of DictWriter
    csvdwr = csv.DictWriter(fp, fieldnames=hname)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSV File Created with dict data --verify")
