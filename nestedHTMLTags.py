
# Nested HTML Tags
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")

print(soup)


# ratings = soup.find_all("div", class_ = "ratings")
# ratings = soup.find_all("div", class_ = "ratings")[3]

# print(ratings)

# print("======Ratings============")
# print(len(ratings))
# rat = soup.find("a")
# rat = ratings.text
# print(rat)
navBAR = soup.find_all("ul", class_ = "nav", id = "side-menu")
computer = navBAR.find_all("il", class_ = "active")[0]
com = computer.find_all("a", class_ ="category-link ")[0]
print(navBAR)
print(len(navBAR))
print(com.text)
