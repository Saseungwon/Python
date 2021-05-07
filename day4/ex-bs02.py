# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2" /> and
<a href="http://example.com/tillie" class="sister">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 문서 파싱
soup = BeautifulSoup(html_doc,"html.parser")

# 구조화하여 출력
print(soup.prettify())

# find : 1개의 태그만 찾음
# find_all : 모든 태그를 찾음
# select_one : 1개의 태그만 찾음
# select : 모든 태그를 찾음
# el = soup.a # 첫 번째 a
# print(el.name)
# print(el)
# print(el.string)
# print(el.text)
# print(el['href'])
els = soup.find_all('a', string=True) # 문자열이 존재하는
for i in els:
    print(i['href'])
# print(els)