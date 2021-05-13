# https://comic.naver.com/webtoon/detail.nhn?titleId=771720&no=1
from selenium import webdriver
import time
import util

wd = webdriver.Chrome('./chromedriver')
url = 'https://comic.naver.com/webtoon/detail.nhn?titleId=771720&no=1'
wd.get(url)
util.fullpage_screenshot(wd, 'webtoon.png')
time.sleep(3)
wd.quit()