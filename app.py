import requests
from bs4 import BeautifulSoup
import csv




def get_page_1(url):
  # boot out the last `<document>`, which contains the binary data
  

  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  f = open("test.txt",'w')
  # links.append(soup.select('div a'))
  for link in soup.find_all('div', class_='product-style'):
    data = link.text
    f.write(data)
    f.write('\n')
  f.close()

def getLinks(base_url, pages):
  # boot out the last `<document>`, which contains the binary data
  
  f = open('test2.txt', 'w')
  for page in range(1,pages):

    page = requests.get(f"{base_url}{page}")
    soup = BeautifulSoup(page.text, 'html.parser')
    for link in soup.find_all('div', class_='product-style'):
      data = link.text
      f.write(data)
      f.write('\n')
    
  f.close()

def getBreweryName(base_url, pages):
  f = open('brewery_names.txt', 'w')
  for page in range(1,pages):

    page = requests.get(f"{base_url}{page}")
    soup = BeautifulSoup(page.text, 'html.parser')
    for name in soup.find_all('a'):
      data = name.text
      f.write(data)
      f.write('\n')
  f.close()
def getBreweryLocation(base_url, pages):
  f = open('brewery_locations.txt', 'w')
  for page in range(1,pages):

    page = requests.get(f"{base_url}{page}")
    soup = BeautifulSoup(page.text, 'html.parser')
    for city in soup.find_all('div', class_='product-producer'):
      data = city.text
      f.write(data)
      f.write('\n')
  f.close()
  
url = 'https://www.brewerydb.com/browse/regional?locationType=any&locality=&region=ohio&countryIsoCode=US'
base_url = "https://www.brewerydb.com/browse/regional/index/locality//region/ohio/countryIsoCode/US/page/"
pages = 7

links = get_page_1(url)
# links2 = getLinks(base_url, pages)
