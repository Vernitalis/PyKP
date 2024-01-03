import scrapy
from urllib.parse import urlencode
import json


class TimetablesSpider(scrapy.Spider):
    name = "timetables"
    allowed_domains = ["portalpasazera.pl"]

    def start_requests(self):
        url = "https://portalpasazera.pl/Wyszukiwarka/ZnajdzPociag"
        credentials = json.loads(getattr(self, "credentials"))

        headers = credentials["headers"]
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {
            "kryteria[O]": "true",
            "kryteria[S]": getattr(self, "id"),
            "kryteria[SK]": getattr(self, "key"),
            "__RequestVerificationToken": credentials["token"],
        }

        for t in ["00:00", "06:00", "12:00", "18:00"]:
            data["kryteria[G]"] = t
            yield scrapy.Request(
                url=url,
                method="POST",
                headers=headers,
                cookies=credentials["cookies"],
                body=urlencode(data),
            )

    def parse(self, response):
        yield json.loads(response.text)
