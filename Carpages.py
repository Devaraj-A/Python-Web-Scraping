import requests
from bs4 import BeautifulSoup
import pandas as pd

page=requests.get('https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7')
soup=BeautifulSoup(page.text, 'lxml')
soup

df=pd.DataFrame({'Link':[''], 'Name':[''], 'Price':[''], 'color':['']})

counter=0
while counter<10:
    cars=soup.find_all('div', class_='media soft push-none rule')
    for car in cars:
        try:
            link=car.find('a', class_='media__img media__img--thumb').get('href')
            link_full='https://www.carpages.ca'+link
            name=car.find('h4', class_='hN').text.strip()
            price=car.find('strong', class_='delta').text.strip()
            color=car.find_all('div', class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
            df=df.append({'Link':link_full, 'Name':name, 'Price':price, 'color':color}, ignore_index =True)
        except:
            pass
    
    next_page=soup.find('a', class_='nextprev').get('href')
    page=requests.get(next_page)
    soup=BeautifulSoup(page.text, 'lxml')
    counter +=1