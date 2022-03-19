import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

driver=webdriver.Chrome('/home/ai/Desktop/chromedriver')
driver.get('https://www.nps.gov/subjects/nationalhistoriclandmarks/list-of-nhls-by-state.htm#onthisPage-46')
soup=BeautifulSoup(page.text, 'lxml')
soup
link=driver.find_elements_by_xpath('//*[@id="0BE01E87-C494-39BF-010C246CE17F44A8-inpage-nav-links"]/ul/li/a')

links=[]
for url in link:
    links.append(url.get_attribute("href"))