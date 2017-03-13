from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

wk = 'https://en.wikipedia.org'

random.seed(datetime.datetime.now())

pages = set()


def getLink(url):
    root = urlopen(wk + url)
    obj = BeautifulSoup(root.read(), 'lxml')
    for link in obj.findAll("a", href=re.compile("^(/wiki/).*")):
        if 'href' in link.attrs:
            href = link.attrs['href']
            # 新页面
            if href not in pages:
                print(href)
                pages.add(href)
                getLink(href)


getLink('')
