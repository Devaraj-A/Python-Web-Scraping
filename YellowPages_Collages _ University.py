import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.yellowpages.com/search?search_terms=college&geo_location_terms=Clearwater%2C+FL'

requests.get(url)

page=requests.get(url)
page

soup=BeautifulSoup(page.text, 'lxml')
soup

df=pd.DataFrame({'Link':[''], 'Collage Name':[''], 'Address':[''], 'Address2':[''], 'Phone':[''], 'Website':[''], 'categories':['']})

while True:
    collages=soup.find_all('div', class_='result')
    for collage in collages:
        try:
            link=collage.find('a', class_='business-name').get('href')
            link_full='https://www.yellowpages.com'+link  
            name=collage.find('a', class_='business-name').text
            address=collage.find('div', class_='street-address').text.strip()
            address2=collage.find('div', class_='locality').text.strip()
            phone=collage.find('div', class_='phones phone primary').text.strip()
            website=collage.find('a', class_='track-visit-website').get('href')
            categories=collage.find('div', class_='categories').text
            df=df.append({'Link':link_full, 'Collage Name': name, 'Address':address, 'Address2':address2, 'Phone':phone, 'Website':website, 'categories':categories}, ignore_index=True)
        except:
            pass
        
    next_page=soup.find('a', class_='next ajax-page').get('href')
    next_full='https://www.yellowpages.com'+next_page
    
    url=next_full
    page=requests.get(url)
    soup=BeautifulSoup(page.text, 'lxml')

df.to_csv('/home/deva/Desktop/Yellow.csv')
