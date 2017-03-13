from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

wk = 'https://en.wikipedia.org'
pages = set()


def getLinks(url):
    target=wk + url
    root = urlopen(target)
    obj = BeautifulSoup(root.read(), 'lxml')
    try:
        print(obj.find("h1").get_text())
        print(obj.find(id="mw-content-text").findAll("p")[0].get_text())
        print(obj.find(class_="mw-editsection")).find("span").find("a")
    except AttributeError:
        print("页面缺失部分属性")
    for link in obj.findAll("a", href=re.compile("^(/wiki/.*)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print("-------------------------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)




getLinks("/wiki/Bing#MSN_Search")

