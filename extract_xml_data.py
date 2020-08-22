'''
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, 
compute the sum of the numbers in the file and ouput the sum.
'''


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input('Enter location: ')
if len(url) < 1: url = 'http://py4e-data.dr-chuck.net/comments_919651.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//comment')
no = t_sum = int(0)
for count in counts:
    no+=1
    no2 = count.find('count').text
    no2 = int(no2)
    t_sum = t_sum + no2

print('Count:', no)
print('Sum:', t_sum)
