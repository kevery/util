from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

root = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")

obj = BeautifulSoup(root.read(), 'lxml')

for link in obj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/).*")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

wk = 'https://en.wikipedia.org'


def getLink(url):
    root = urlopen("%s/wiki/Kevin_Bacon" % (wk))
    print(root)


getLink('/wiki/San_Diego_Comic-Con')
