import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Chrome('/home/ai/Desktop/chromedriver')
driver.get('https://www.nps.gov/subjects/nationalhistoriclandmarks/list-of-nhls-by-state.htm#onthisPage-46')
soup=BeautifulSoup(page.text, 'lxml')
link=driver.find_elements_by_xpath('//*[@id="0BE01E87-C494-39BF-010C246CE17F44A8-inpage-nav-links"]/ul/li/a')

links=[]
for url in link:
    links.append(url.get_attribute("href"))
