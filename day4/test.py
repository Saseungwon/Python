from bs4 import BeautifulSoup
import urllib.request

from  selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# javascript:moveMainFrame('0410');
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://data.kleague.com/')
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/ul/li[1]/a').click()
menu = driver.find_element_by_css_selector('.main-menu')
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
form = soup.find_all('form')
for i in form:
    print(i)
