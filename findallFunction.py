# findall Function in Python for WebScraping

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, "lxml")
print(soup)

prices = soup.find_all("h4", class_ = "pull-right price")
print(len(prices))

for i in prices:
    print(i)

# Incase you just wanna get the text only
for i in prices:
    print(i.text)

# print(prices[3]) # Should give us an error
print("Printing with help of index")
print(prices[2])
print(prices[2].text) # Should give us a last item as there are only 3