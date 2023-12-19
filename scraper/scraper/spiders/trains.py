#!/usr/bin/env python3

from scrapy import Spider
from scrapy.http import JsonRequest

def create_find_train_request(station_id: str, key: str, time: str, token: str, headers={}, departure=True):
    url = "https://portalpasazera.pl/Wyszukiwarka/ZnajdzPociag"
    data = {
        "kryteria[O]": str(departure).lower(),
        "kryteria[S]": station_id,
        "kryteria[SK]": key,
        "kryteria[G]": time,
        "__RequestVerificationToken": token
    }
    return JsonRequest(url=url, data=data)

class TrainSpider(Spider):
    name = "trains"
    def start_requests(self):
        headers = self.settings.getdict("DEFAULT_REQUEST_HEADERS")
        token = self.settings.get("PP_BODY_TOKEN")
        yield create_find_train_request("50500", "c2d", "06:00", token, headers=headers)

    def parse(self, response):
        yield {"response": response.text}
