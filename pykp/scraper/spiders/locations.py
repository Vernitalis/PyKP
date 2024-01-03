from os import setreuid
import scrapy
import json
from urllib.parse import urlencode
from pykp.scraper.items import LocationItem


class LocationsSpider(scrapy.Spider):
    name = "locations"
    allowed_domains = ["portalpasazera.pl"]

    def start_requests(self):
        url = (
            "https://portalpasazera.pl/MapaOL/PodajDaneStartoweMapyDlaDanegoWyszukania"
        )

        credentials = json.loads(getattr(self, "credentials"))

        headers = credentials["headers"]
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {
            "PID": getattr(self, "pid"),
            "SID": getattr(self, "sid"),
            "calaTrasa": "",
            "__RequestVerificationToken": credentials["token"],
        }

        yield scrapy.Request(
            url=url,
            method="POST",
            headers=headers,
            cookies=credentials["cookies"],
            body=urlencode(data),
        )

    def parse(self, response):
        data = json.loads(response.text)
        for item in data[0]["ListaStacjiPociagu"]:
            yield LocationItem(station_id=item["StacjaID"], x=item["X"], y=item["Y"])

