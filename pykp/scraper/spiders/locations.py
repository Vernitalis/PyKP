import scrapy
import json
from ..items import LocationItem
from ..requests import UrlEncodedRequest


class LocationsSpider(scrapy.Spider):
    name = "locations"
    allowed_domains = ["portalpasazera.pl"]
    url = "https://portalpasazera.pl/MapaOL/PodajDaneStartoweMapyDlaDanegoWyszukania"

    def start_requests(self):
        credentials = json.loads(getattr(self, "credentials"))
        data = {
            "PID": getattr(self, "pid"),
            "SID": getattr(self, "sid"),
            "calaTrasa": "",
            "__RequestVerificationToken": credentials["token"],
        }

        yield UrlEncodedRequest(
            url=self.url,
            headers=credentials["headers"],
            cookies=credentials["cookies"],
            data=data,
        )

    def parse(self, response):
        data = json.loads(response.text)
        for item in data[0]["ListaStacjiPociagu"]:
            yield LocationItem(station_id=item["StacjaID"], x=item["X"], y=item["Y"])
