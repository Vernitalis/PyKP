import scrapy
import json
from pykp.scraper.requests import UrlEncodedRequest


class TimetablesSpider(scrapy.Spider):
    name = "timetables"
    allowed_domains = ["portalpasazera.pl"]
    url = "https://portalpasazera.pl/Wyszukiwarka/ZnajdzPociag"

    def start_requests(self):
        credentials = json.loads(getattr(self, "credentials"))
        data = {
            "kryteria[O]": "true",
            "kryteria[S]": getattr(self, "id"),
            "kryteria[SK]": getattr(self, "key"),
            "__RequestVerificationToken": credentials["token"],
        }

        for t in ["00:00", "06:00", "12:00", "18:00"]:
            data["kryteria[G]"] = t
            yield UrlEncodedRequest(
                url=self.url,
                headers=credentials["headers"],
                cookies=credentials["cookies"],
                data=data,
            )

    def parse(self, response):
        yield json.loads(response.text)
