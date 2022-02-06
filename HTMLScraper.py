# %%
#import libraries

from email import message
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from http import server
from bs4 import BeautifulSoup as bs
import requests
import urllib.request

# %%
url = 'THE URL YOU WANT'
#Get the below info from https://httpbin.org/get
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0","Accept-Encoding":"gzip, deflate, br","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Dnt": "1","Connection":"close","Upgrade-Insecure-Requests":"1"}
html = urllib.request.urlopen(url)

#identify the get request and variable
def getdata(url):
    r = requests.get(url)
    return r.text

# %%
#parse the html
htmldata = getdata("YOUR URL")
soup = bs(htmldata, 'html.parser')
data = ''


# %%
#just scraping for text value in the section of html called "blockquote", change it for the html bracket you want
for data in soup.find_all("blockquote"):
    dailymsg = print(data.get_text(), file=open('dailyquote.txt', 'a'))

# %%
#show your work
print(data.get_text())


# %%



