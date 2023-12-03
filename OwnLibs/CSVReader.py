import csv

def read_csv(csv_file):
    data = []
    with open(csv_file, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    if len(data) == 1 and "address" in csv_file:
        return data[0]
    else:
        return data

#print(read_csv("../Data/login.csv"))