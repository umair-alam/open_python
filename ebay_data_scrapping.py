#use this code to scrape data from eBay. This is just a starter code that only scrap data such as product name, 
#it's cost, and shipping details only. Further data is yet to be scrapped. Thank you.


import ssl
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url='https://www.ebay.com/b/Mens-Casual-Shoes/24087/bn_57235'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

filename = "c:/Users/umair/OneDrive/Desktop/Python Practice/Product_Phone3.csv"
f = open(filename,"w")
header = "Name, Price, Shipping\n"
f.write(header)

uClient = uReq(my_url,context=ctx)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,'html.parser')

containers = page_soup.findAll("div",{"class":"s-item__wrapper clearfix"})

for container in containers:
    price_noww = container.findAll("div",{"class":"s-item__detail s-item__detail--primary"})
    price_now = price_noww[0].text
    
   
    price_shipp = container.findAll("span",{"class":"s-item__shipping s-item__logisticsCost"})
    price_shipping = price_shipp[0].text
    
    
    
    s=container.h3.text.replace(",","||")
    f.write(s)
    f.write(",")
    f.write(price_now)
    f.write(",")
    f.write(price_shipping)
    f.write("\n")

f.close()
