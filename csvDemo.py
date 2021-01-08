import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    #print(csvReader)
    #print(list(csvReader))

    names = []
    stats = []

    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])
    print(names)
    print(stats)

with open('utilities/loanapp.csv','a',newline='') as wFile:
    writer = csv.writer(wFile)
    writer.writerow(['Bob', 'rejected'])
    writer.writerow(['Erik', 'approved'])
