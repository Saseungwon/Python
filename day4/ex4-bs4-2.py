# -*- coding:utf-8 -*-
from itertools import count

from bs4 import BeautifulSoup
import urllib.request

from numpy.linalg import cond

url = 'https://movie.daum.net/ranking/boxoffice/weekly'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# 영화제목, 링크, 평점 ...
tb = soup.select_one('.list_movieranking')
trs = tb.find_all('li')

imgUrl = ''
content = ''
title = ''
grade = ''

movielist=[]
import os
path = os.getcwd() + '/image'
print(path)
for li in trs:
    try:
        imgs = li.select_one('.poster_movie img')
        if imgs != None:
            imgUrl = imgs['src']
            title  = imgs['alt']
            urllib.request.urlretrieve(imgUrl,path + '/' + title + '.jpg')
        el = li.select_one('.poster_info a')
        content = el.text.strip() # 영화내용
        # 등급 관객수
        grade = li.select_one('.ico_movie.ico_see').getText()
        thumb = li.select_one('.thumb_cont')
        span = thumb.find_all('span')[3]
        countText = span.getText()
        countText = countText.replace('관객수', '')
        count = countText.replace('명', '')
        movielist.append([imgUrl, content, grade, count])


    except Exception as e:
        print(str(e))
print(movielist)