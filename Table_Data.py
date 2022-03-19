import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.nfl.com/standings/conference/2021/REG'

page=requests.get(url)
page

soup=BeautifulSoup(page.text, 'lxml')
soup

table=soup.find('table', {'summary':'Standings - Detailed View'})
table

table.find_all('th')

headers = []
for i in table.find_all('th'):
    titles=i.text.strip()
    headers.append(titles)
    
    df=pd.DataFrame(columns=headers)

for j in table.find_all('tr')[1:]:
    first_td=j.find_all('td')[0].find('div', class_='d3-o-club-shortname').text.strip()
    row=j.find_all('td')[1:]
    rowdata=[tr.text.strip() for tr in row]
    rowdata.insert(0, first_td)
    length=len(df)
    df.loc[length]=rowdata    
    
    