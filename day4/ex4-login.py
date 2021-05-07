from  selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.msn.com/ko-kr/')

try:
    cnt = 20
    elem = driver.find_element_by_tag_name('body')
    pagedowns = 1
    while pagedowns <cnt:
        # PAGE_DOWN(스크롤)에 따라서 결과 값이 달라진다.
        elem.send_keys(Keys.PAGE_DOWN)
        # 페이지 스크롤 타이밍을 맞추기 위해 sleep
        time.sleep(1)
        pagedowns += 1
except Exception as e:
    print(e)