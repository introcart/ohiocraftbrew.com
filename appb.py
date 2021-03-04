import requests
from bs4 import BeautifulSoup
import csv

def get_page_1(url):
  # boot out the last `<document>`, which contains the binary data
  

  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  f = open("ocb.txt",'w')
  # links.append(soup.select('div a'))
  for link in soup.find_all('strong'):
    data = link.text
    f.write(data)
    f.write('\n')
  for link in soup.find_all('img'):
    data = link['src']
    f.write(data)
    f.write('\n')
  f.close()


url = 'https://ohiocraftbeer.org/ohio-breweries/'