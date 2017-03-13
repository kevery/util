from urllib.request import urlopen
from bs4 import BeautifulSoup
wk = 'http://www.qq.com/'
html = urlopen(wk)
bsobj = BeautifulSoup(html.read(), 'lxml')
print(bsobj)
price = bsobj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()
print(bsobj.findAll(lambda x: len(x.attrs) == 2))
