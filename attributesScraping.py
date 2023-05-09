import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
print(soup)

head = soup.header
print(head)
headAttributes = head.attrs
print(head.attrs)
print(headAttributes['class'])
print(headAttributes['role'])
print(soup.div.attrs)
