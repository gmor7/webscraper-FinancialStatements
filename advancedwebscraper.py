# Exports the following financials to csv file:
    # total debt/total liabilities
    # current assets
    # current liabilities
    # EPS for last five years
    # market cap
    # book value

import requests
from bs4 import BeautifulSoup
import lxml
import csv

header = []
url = 'https://www.hl.co.uk/shares/shares-search-results/h/hochschild-mining-plc-ordinary-25p/financial-statements-and-reports'
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")
print(table)

with open('prices.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerow(header)

    for tr in table.find_all('tr'):
        row = [td.get_text(strip=True) for td in tr.find_all('td')]
        csv_output.writerow(row)

