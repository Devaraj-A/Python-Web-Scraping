"""
Created on Sun Dec  5 12:44:32 2021

@author: ai
"""
import requests
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

chrome=webdriver.Chrome('/home/ai/Desktop/chromedriver')
chrome.get('https://in.puma.com/in/en/mens/mens-shoes/mens-shoes-sneakers')
chrome.maximize_window()

show_all=chrome.find_element_by_xpath("//button[@class='btn btn-primary show-all-button col-12 col-sm-4 col-md-2 ml-sm-2 ']")
show_all.click()
time.sleep(3)
page_sh=chrome.execute_script('return document.body.scrollHeight')
while True:
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    newpage_sh=chrome.execute_script('return document.body.scrollHeight')
    if newpage_sh == page_sh:
        break
    page_sh = newpage_sh
soup=BeautifulSoup(chrome.page_source, 'lxml')
df=pd.DataFrame({'Name':[''],'Colors':[''], 'Standerd_Price':[''], 'New_price':[''], 'Link':['']})
product=soup.find_all('div', class_='product-tile')
for pro in product:
    name=pro.find('a', class_='product-tile-title product-tile__title pdp-link line-item-limited line-item-limited--2').text
    color=pro.find('p', class_='swatch-title product-tile__swatch-title swatch-title-carousel').text.strip()
    try:
        price_standerd=pro.find('div', class_='product-tile-price-standard product-tile__price--standard').text
    except:
        price_standerd='N/A'
    try:
        price_new=pro.find('div', class_='product-tile-price-new product-tile__price--new').text
    except:
        price_new='N/A'
    link=pro.find('a', class_='product-tile-title product-tile__title pdp-link line-item-limited line-item-limited--2').get('href')
    link_full='https://in.puma.com'+link
    df=df.append({'Name':name,'Colors':color, 'Standerd_Price':price_standerd, 'New_price':price_new, 'Link':link_full}, ignore_index=True)
    
    df=to_csv('/home/Desktop/Puma.xlsx')
