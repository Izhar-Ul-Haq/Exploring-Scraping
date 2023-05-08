import requests
import bs4
import selenium
from bs4 import BeautifulSoup
url = "https://courses.wscubetech.com"
r = requests.get(url)
print(r)
print()
soup = BeautifulSoup(r.text, "lxml")
print(soup)