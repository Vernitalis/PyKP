from itemadapter.adapter import ItemAdapter
from scrapy.utils.defer import maybe_deferred_to_future
from scrapy.http.request.json_request import JsonRequest
from scrapy.exceptions import CloseSpider
import json
import os


class EnvironmentVariableOutput:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.items.append(adapter.asdict())
        return item

    def close_spider(self, spider):
        variable_name = "PYKP_{name}_OUTPUT".format(name=spider.name.upper())
        output = json.dumps(self.items)
        os.environ[variable_name] = output


class HttpUploadItems:
    async def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        request = JsonRequest(spider.upload_url, data=adapter.asdict())
        try:
            response = await maybe_deferred_to_future(
                spider.crawler.engine.download(request)
            )
            if response.status != 200:
                raise Exception
        except Exception:
            raise CloseSpider("An error during uploading the items has occured")
        return item
