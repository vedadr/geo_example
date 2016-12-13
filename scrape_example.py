from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series, DataFrame

url = 'http://fzs.ba/'

result = requests.get(url)
c = result.content

soup = BeautifulSoup(c)

summary = soup.find('table', {'class': 'grafinfo'})
# tables = summary.find_all('table')
data = []
rows = summary.find_all('tr')
# table_rows = summary.find_all('td')
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text = td.find(text=True)
        print(text)
        data.append(text)

# lets break it into two different arrays
variable_name = []
variable_value = []
for index, el in enumerate(data):
    if el[1].isdigit():
        variable_name.append(data[index - 1])
        variable_value.append(el)

table_df = pd.concat([Series(variable_name), Series(variable_value)], axis=1)
table_df.columns = ['Variable_name', 'Value']
print("test")