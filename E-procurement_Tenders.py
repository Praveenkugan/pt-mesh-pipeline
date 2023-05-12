import requests
from bs4 import BeautifulSoup
import csv

url = 'https://etenders.gov.in/eprocure/app'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tender_table = soup.find('table', class_='list_table')

tender_rows = tender_table.find_all('tr')

with open('tender_details.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)


    for row in tender_rows[1:]:  # Skip the first row (header row)
        cells = row.find_all('td')

        if len(cells) >= 4:
            tender_title = cells[0].text.strip()
            reference_no = cells[1].text.strip()
            closing_date = cells[2].text.strip()
            bid_opening_date = cells[3].text.strip()

            writer.writerow([tender_title, reference_no, closing_date, bid_opening_date])
        else:
            print("Skipping row: Insufficient data")
            for cell in cells:
                print(f"Cell content: {cell.text.strip()}")

print("Tender details saved to tender_details.csv file.")
