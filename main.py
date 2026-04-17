import requests
a="https://hacker-news.firebaseio.com/v0/item/47804965.json?print=pretty"
response=requests.get(a)
data=response.json()
print(data["title"])
