from bs4 import BeautifulSoup
import urllib.request
url = 'http://www.google.com/'
with urllib.request.urlopen(url) as response:
    html = response.read()
    print(response.read)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify()) #구조화되게 프린트