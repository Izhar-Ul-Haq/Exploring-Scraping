import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
print(soup)


names = soup.find_all("a", class_ = "title")
print(names)
print("================")

# For Names of the Products
product_list = []
for name in names:
    i = name.text
    product_list.append(i)

print(product_list)

print("===================")
# For Price of the Products

product_prices  = []

prices = soup.find_all("h4", class_ = "pull-right price")

for price in prices:
    x = price.text
    product_prices.append(x)
print(product_prices)
print("==============")
for i in product_prices:
    print(i)
print("description")
desc = soup.find_all("p", class_ = "description")
print(desc)

desc_list = []

for des in desc:
    de = des.text
    desc_list.append(de)
print(desc_list)

print("The Length of the Product Names is:", len(product_list))
print("The Length of the Product Prices list is:", len(product_prices))
print("The Length of the Product descripotion:", len(desc_list))

# Review

review_list = []

reviews  = soup.find_all("p", class_ = "pull-right")

for review in reviews:
    rev = review.text
    review_list.append(rev)

print(review_list)
for y in review_list:
    print(y)
    
print(len(review_list))
print("============Data Frame Pandas============")
df = pd.DataFrame(
    {
        "Product Name": product_list,
        "Product Description": desc_list,
        "Product Review": review_list,
        "Product Prices": product_prices
    }
)
print(df)
    