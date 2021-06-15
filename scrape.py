from bs4 import BeautifulSoup
import requests

URL= ""

source = requests.get(URL).text

site = BeautifulSoup(source,'lxml')

headers = site.find_all('header',class_='entry-header')

for header in headers:
    print(header.text)