import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

driver=webdriver.Chrome('/home/ai/Documents/chromedriver_linux64/chromedriver')
driver.get('https://store.unionlosangeles.com/collections/outerwear')
driver.maximize_window()

scroll_height=driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_scrll=driver.execute_script('return document.body.scrollHeight')
    if new_scrll == scroll_height:
        break
    scroll_height = new_scrll
    
df=pd.DataFrame({'Name':[''],'Title':[''],'Price':[''],'Link':['']})
    
soup=BeautifulSoup(driver.page_source, 'lxml')
section=soup.find('div', {'id':'main','role':'main'})

dresses=section.find_all('li')
for dress in dresses:
    link=dress.find('a').get('href')
    name=dress.find(class_='cap-vendor').text
    title=dress.find(class_='cap-title').text
    price=dress.find(class_='cap-price').text
    df=df.append({'Name':name,'Title':title,'Price':price,'Link':link}, ignore_index=True)

df['Link'][4:]='https://store.unionlosangeles.com'+df['Link'][4:]
