import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://en.wikipedia.org/wiki/List_of_companies_of_India')

df = pd.read_html(driver.page_source)[1]
print(df.head())

driver.close()
