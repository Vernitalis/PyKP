#!/usr/bin/env python3

from scrapy import Spider
import urllib.parse as url
from scraper.items import StationItem

letters = "aąbcćdeęfghijklłmnńoóprstuyzźż"
# letters = "b"
catalog_base_url = "https://portalpasazera.pl/KatalogStacji"
search_base_url = "https://portalpasazera.pl/Wyszukiwarka/WyszukajStacje"

class StationsSpider(Spider):
    name = "stations"
    start_urls = ["{url}?{query}".format(url=catalog_base_url, query=url.urlencode({"nazwa": l})) for l in letters]

    def find_station(self, response):
        for station in response.json():
            station_item = StationItem(id=station["ID"], name=station["Nazwa"], iso=station["Iso"], key=station["Key"], nz=station["NZ"])
            yield station_item

    def parse(self, response):
        names = response.xpath("//div[@id=\"stacjaResultsDefault\"]//div[@class=\"row\"]/div//h3/span/text()")
        page_amount = int(response.xpath("//ul[@class=\"pagination \"]/li[last()-1]/a/text()").get())
        pages_range = range(2, page_amount + 1)
        parsed_url = url.urlparse(response.url)
        query = url.parse_qs(parsed_url.query)
        next_urls = []
        for page_number in pages_range:
            query_copy = query.copy()
            query['p'] = page_number
            query_string = url.urlencode(query, doseq=True)
            new_url = (parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, query_string, parsed_url.fragment)
            encoded_url = url.urlunparse(new_url)
            next_urls.append(encoded_url)

        for station in names.getall():
            params = {"wprowadzonyTekst": station}
            encoded_url = search_base_url + "?" + url.urlencode(params)
            yield response.follow(encoded_url, callback=self.find_station)
            # yield {"name": station}

        for request in response.follow_all(next_urls, callback=self.parse):
            yield request
