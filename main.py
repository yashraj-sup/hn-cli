import requests
a="https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
response=requests.get(a)
data=response.json()
for i in range(5):
    story_id=data[i]
    f=f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    r=requests.get(f)
    story=r.json()
    print(story["title"])

