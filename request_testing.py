import requests
import json


class TestRequest:
    def start(self):
        r = requests.get("https://api.tvmaze.com/search/shows", params={"q": "Star Wars"})
        if r.status_code == 200:
            data = json.loads(r.text)
            for show in data:
                print(show['show']['name'])
        else:
            print(f"Error: {r.status_code}")
