from selenium import webdriver

import time

url = 'http://tour.interpark.com/'
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
time.sleep(1)
driver.get(url)
driver.find_element_by_id('SearchGNBText').send_keys('하와이')
driver.find_element_by_css_selector('button.search-btn').click()
driver.implicitly_wait(3)
html = driver.page_source
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
time.sleep(3)
div = soup.find('.boxlilst')
li = div.find_all('li')
for i in li:
    print(i)