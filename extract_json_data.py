#Exercise python for web data course on coursera
#Extracting Data from json, prompting a link for user and extract data

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_919652.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
info = info['comments']
no = t_sum = int(0)
for item in info:
    no+=1
    no2 = item['count']
    no2 = int(no2)
    t_sum = t_sum + no2
print('Count:', no)
print('Sum:', t_sum)
