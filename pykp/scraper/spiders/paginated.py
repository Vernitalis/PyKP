import scrapy
import urllib.parse

class PaginatedSpider(scrapy.Spider):

    def parse(self, response):
        page_amount = int(response.xpath("//ul[@class=\"pagination \"]/li[last()-1]/a/text()").get())
        parsed_url = urllib.parse.urlparse(response.url)
        query = urllib.parse.parse_qs(parsed_url.query)
        for page_number in range(1, page_amount + 1):
            query['p'] = page_number
            query_string = urllib.parse.urlencode(query, doseq=True)
            new_url = (parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, query_string, parsed_url.fragment)
            encoded_url = urllib.parse.urlunparse(new_url)
            yield response.follow(encoded_url, callback=self.parse_page)

    def parse_page(self, response) -> scrapy.Request | scrapy.Item | None:
        pass
