import csv

with open("periodicTable.csv", newline='') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        rowString = ",".join(row)
        info = rowString.split(";")
        print(info)
