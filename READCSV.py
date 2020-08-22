import csv
def leercsv():
    with open('filecsv.csv', newline='') as File:
        print("ESTRUCTURA CSV", type(File))
        reader = csv.reader(File)
        for row in reader:
            print(row)
