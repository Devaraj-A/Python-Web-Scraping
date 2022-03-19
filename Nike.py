from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

driver=webdriver.Chrome('/home/ai/Documents/Spyder/Selenium/chromedriver')
driver.get('https://www.nike.com/in/w/sale-3yaep')
driver.maximize_window()

pageheight = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(10)
    newheight=driver.execute_script('return document.body.scrollHeight')
    if newheight == pageheight:
        break
    pageheight = newheight
    
soup=BeautifulSoup(driver.page_source, 'lxml')
product=soup.find_all('div', class_='product-card css-1lukt7x css-z5nr6i css-11ziap1 css-14d76vy css-dpr2cn product-grid__card')
df=pd.DataFrame({'Name':[''], 'Price_full':[''], 'Price_sales':[''], 'Link':['']})
for pro in product:
    try:
        link=pro.find('a', class_='product-card__link-overlay').get('href')
        name=pro.find('div', class_='product-card__title').text
        price_full=pro.find('div', class_='product-price is--striked-out').text
        price_sale=pro.find('div', class_='product-price is--current-price css-s56yt7').text   
        df=df.append({'Name':name, 'Price_full':price_full, 'Price_sales':price_sale, 'Link':link}, ignore_index=True)
    except:
        pass