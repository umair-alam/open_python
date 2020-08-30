'''
Reading website data, Web scraping
usage of BeautifulSoup
'''

import re
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup as bs
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter - ')
    if len(url) < 1 : break #url = 'http://py4e-data.dr-chuck.net/comments_362967.html'
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = bs(html, 'html.parser')
    num_list = list()
    count = 0
    #separate all span tags from the data
    span_tag = soup('span')
    for spans in span_tag:
        x = re.findall('[0-9]+', str(spans)) #to mitigate the error "TypeError: expected string or bytes-like object" while..
        #searching <span as it was starting with "<" tag
        count +=1
        for num in x:
            num_list.append(int(num))
    print("Count", count)
    print("Sum", sum(num_list))
