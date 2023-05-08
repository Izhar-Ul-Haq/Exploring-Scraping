import requests
url = "https://www.google.com"
r = requests.get(url)
print(r)
print(r.status_code)
print(r.text)
print(r.headers)
print(r.headers['content-type'])
print(r.json)