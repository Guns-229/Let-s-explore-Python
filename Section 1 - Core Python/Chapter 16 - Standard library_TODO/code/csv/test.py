import csv

with open("test.csv", newline="") as fp:
    data = csv.DictReader((line.replace('\0', '')
                        for line in fp), escapechar='\\')
    for d in data:
        print(d)
