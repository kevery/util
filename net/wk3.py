import random
import re
from urllib.parse import urlparse
from urllib.request import urlopen

from bs4 import BeautifulSoup


# Retrieves a list of all Internal links found on a page
def getInternalLinks(bsobj, includeurl):
    urltuple = urlparse(includeurl)
    includeurl = urltuple.scheme + "://" + urltuple.netloc
    internalLinks = []
    # 找出所有以'/'开头的链接
    for link in bsobj.findAll("a", href=re.compile(" ^(/ |.*" + includeurl + ")")):
        href = link.attrs['href']
        if href is not None:
            if href not in internalLinks:
                if href.startswith("/"):
                    print(includeurl + href)
                    internalLinks.append(includeurl + href)
                else:
                    print(href)
                    internalLinks.append(href)
    return internalLinks


# Retrieves a list of all external links found on a page
def getExternalLinks(bsobj, excludurl):
    externalLinks = []
    # find all links that begin with 'http' or 'www' that do
    # not contain the current url
    for link in bsobj.findAll("a", href=re.compile("^(http|www)(?!" + excludurl + ").*$")):
        href = link.attrs['href']
        if href is not None:
            if href not in externalLinks:
                externalLinks.append(href)
    return externalLinks


# get random externalLink from startLink
def getRandomExternalLinks(startPage):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    html = urlopen(startPage)
    bsobj = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bsobj, urlparse(startPage).netloc)
    if len(externalLinks) == 0:
        print("no external links,looking around the site for one")
        domain = urlparse(startPage).scheme + urlparse(startPage).netloc
        internalLinks = getInternalLinks(bsobj, domain)
        return getRandomExternalLinks(internalLinks[random.randint(0, len(internalLinks) - 1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://163.com")
