from selenium import webdriver
import time
import webbrowser
import util

wd = webdriver.Chrome('./chromedriver.exe')
url = 'http://naver.com'
wd.get(url)
util.fullpage_screenshot(wd, "test.png")
time.sleep(3)
wd.quit()