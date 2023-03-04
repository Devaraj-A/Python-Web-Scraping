import requests
from bs4 import BeautifulSoup
import pandas as pd
class Webscraper:
  def __init__(self,url):
    self.url = url

  @property
  def requests(self):
    return requests.get(self.url)

  @property
  def scrape(self):
    website = requests.get(self.url)
    data = BeautifulSoup(website.text, 'lxml')
    table = data.find('table',{'id':input('Table id:')})
    header = []
    for i in table.find_all('th'):
      row = i.text
      header.append(row)

    df = pd.DataFrame(columns=header)

    for j in table.find_all('tr')[1:]:    
      data = j.find_all('td')
      ap = [k.text for k in data]
      length = len(df)
      df.loc[length]=ap
  
    return df

  @requests.setter
  def results(self,url):
    self.url = url

data = Webscraper(input('Enter The Website:'))
data.scrape
