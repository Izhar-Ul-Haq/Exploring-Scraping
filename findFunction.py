import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, "lxml")
print(soup)
print("To Print Div Tags")
print(soup.find("div"))
print("======================")
print(soup.find("a",{"class":"btn-menu2"}))
print("======================")
print(soup.find("a", {"href", "how-to-videos"}))
print("======================")
print(soup.find("a", {"class":"btn-menu1 install-extension"}))
print("======================")
print("======================")
print(soup.find("p", class_ = "description"))