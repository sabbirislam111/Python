import csv
with open('./data/currencyrates.csv', 'r') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Bangladeshi' in line[0]:
            usd = (line[2])
            cnv = (1*usd)
    print(cnv)