import requests
import re

text = '<a href = "www.baidu.com">....'
urls = re.findall('<a href = (.*?)>', text, re.S)
for u in urls:
    print(u)

html = '''
<html>
<title>爬虫的基本知识</title><title>爬虫的基本知识22</title>
<body>
……
</body>
</html>
'''
print(re.search('<title>(.*?)</title>', html, re.S).group(1))
html = '''
<html>
<title>爬虫的基本知识</title>
<body>
……
</body>
</html>
'''

Pages = 'http://tieba.baidu.com/p/4342201077?pn=1'
for i in range(10):
    print(re.sub('pn=\d', 'pn=%d' % i, Pages))


