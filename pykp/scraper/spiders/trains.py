import scrapy
from pykp.scraper.items import TrainItem
from pykp.scraper.spiders.paginated import PaginatedSpider


class TrainsSpider(PaginatedSpider):
    name = "trains"
    allowed_domains = ["portalpasazera.pl"]
    start_urls = ["https://portalpasazera.pl/WynikiWyszukiwania/ZnajdzPociag?sid=Yscc2FfZuluscc2Feumvag8p1eYrVLkFOwdrCy30fWSLozlULG69scc2FUneX5xv30ZF2ILG8YWe8rmnKLagOtAxkgXIQlcWRZNepCvjGj8PPSczR53dQn4PCnpMGkQ0FeIA4v8kT7TP"]

    @staticmethod
    def prepare(s: scrapy.Selector):
        text = s.get()
        if text is None:
            return ""
        return text.strip()

    def parse_page(self, response):
        rows = response.xpath('//div[@class="row catalog-table__row abt-focusable"]')
        for row in rows:
            fields = row.xpath('./div')
            departure=self.prepare(fields[0].xpath('./h3/text()[3]'))
            platform=self.prepare(fields[1].xpath('./strong/text()'))
            track=self.prepare(fields[2].xpath('./strong/text()'))
            carrier=self.prepare(fields[3].xpath('./strong/text()'))
            name=self.prepare(fields[4].xpath('./strong/text()'))
            id=self.prepare(fields[5].xpath('./strong/text()'))
            start=self.prepare(fields[6].xpath('./strong/span[1]/text()'))
            destination=self.prepare(fields[6].xpath('./strong/span[2]/text()'))
            url=self.prepare(row.xpath("./a/@href"))
            item = TrainItem(departure=departure, platform=platform, track=track, carrier=carrier, name=name, id=id, start=start, destination=destination, url=url)
            yield item

