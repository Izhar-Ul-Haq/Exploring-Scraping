import requests
from bs4 import BeautifulSoup
url = "https://courses.wscubetech.com"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
print(soup.div)
print(soup.find_parent)


