import csv

def input_from_csv(input):
    filename = "digital_twin\\"+input+".csv"

    fields = []
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)
    return rows