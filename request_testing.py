import requests
import json


class TestRequest:
    def __init__(self):
        tv_shows = self.__get_tv_shows("Star Wars")
        for show in tv_shows:
            print(show['show']['name'])

    def __get_tv_shows(self, title):
        response = requests.get("https://api.tvmaze.com/search/shows", params={"q": title})
        return json.loads(response.text) if response.status_code == 200 else []
