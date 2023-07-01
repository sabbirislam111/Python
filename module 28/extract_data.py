import requests
from bs4 import BeautifulSoup
import re
import csv

data = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(data).text.encode('utf-8').decode('ascii', 'ignore')

soup = BeautifulSoup(text , 'lxml')
table = soup.find('table', class_='wikitable')
print(table)

rows = table.find_all('tr')[1:]
duplicate_handel = {}
for row in rows:
    data = row.find_all(['th', 'td'])
    try:
        version_text = data[5].a.text.split(' ')[1] 
        version_number = re.sub(r'\D', "", version_text)
        price_text = data[-1].text.split('/')[-1]
        only_price = re.sub(r'\D', "", price_text)
        if only_price > only_price[0]:
            if version_number:
                duplicate_handel[version_number] = only_price
    except:
        pass


csvFiles = ['version', 'price']
with open('write.csv', 'w', newline='') as csvFile:
    write_csv = csv.writer(csvFile)
    write_csv.writerow(csvFiles)

    for key, value in duplicate_handel.items():
        write_csv.writerow([key, value])
    csvFile.close()
