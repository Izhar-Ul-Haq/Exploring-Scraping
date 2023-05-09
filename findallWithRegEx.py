# findall function in python for scraping and regex
import requests
from bs4 import BeautifulSoup
import re
url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)

print(r)

soup = BeautifulSoup(r.text, "lxml")
print(soup)

data3 = soup.find_all(string = "Glaxay tab 6")
print(data3)

data1 = soup.find_all(string = "Copyright &copy 2023")
print(data1)

data3 = soup.find_all(string = "Acer Extensa 15 (2540) Black")
print(data3)

data = soup.find_all(sting = re.compile("Le"))
print(data)