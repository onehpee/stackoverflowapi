import requests
import json

respnse = requests.get("http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

for data in (respnse.json()["items"]):
    print(data["title"])
    print(data["link"])
    print()