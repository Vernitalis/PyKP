from pykp.scraper.items import StationItem
from pykp.scraper.spiders.paginated import PaginatedSpider


letters = "aąbcćdeęfghijklłmnńoóprstuyzźż"

class StationsSpider(PaginatedSpider):
    name = "stations"
    allowed_domains = ["portalpasazera.pl"]
    start_urls = ["https://portalpasazera.pl/KatalogStacji?nazwa={name}".format(name=l) for l in letters]

    def search_station(self, response):
        for station in response.json():
            station_item = StationItem(id=station["ID"], name=station["Nazwa"], iso=station["Iso"], key=station["Key"], nz=station["NZ"])
            yield station_item

    def parse_page(self, response):
        names = response.xpath("//div[@id=\"stacjaResultsDefault\"]//div[@class=\"row\"]/div//h3/span/text()")

        for name in names.getall():
            url = "https://portalpasazera.pl/Wyszukiwarka/WyszukajStacje?wprowadzonyTekst={name}".format(name=name)
            yield response.follow(url, callback=self.search_station)

