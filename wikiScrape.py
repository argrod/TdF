import requests, urllib3, selenium, io

import pandas as pd

from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/List_of_Tour_de_France_general_classification_winners")
 
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
 
# display scraped data
print(soup.prettify())

print(soup.find_all('table')[2])

pd.read_html(str(soup.find_all('table')[2]))

pd.read_html(str(soup.find_all('table')[1]))

test = pd.read_html(str(soup.find_all('table')[1]))

test = str(test).split('\n')[1:]
pd.read_csv(io.StringIO('\n'.join(test)),header = None)

# print('Classes of each table:')
# for table in soup.find_all('table'):
#     print(table.get('caption'))

soup.find_all('table')[0].get('class')
table = soup.find_all('table')[0]
table_body = table.find('tbody')
table_body.find_all('tr')